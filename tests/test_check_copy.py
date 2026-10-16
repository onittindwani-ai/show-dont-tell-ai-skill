import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import check_copy as cc  # noqa: E402

SCRIPT = os.path.join(ROOT, "scripts", "check_copy.py")


def examples():
    """Return (name, before, after) for every example in references/EXAMPLES.md."""
    with open(os.path.join(ROOT, "references", "EXAMPLES.md"), encoding="utf-8") as fh:
        text = fh.read()
    out = []
    for block in re.split(r"\n## ", text)[1:]:
        name = block.splitlines()[0]
        parts = re.split(r"\*\*After\*\*", block)
        before = "\n".join(l[2:] for l in parts[0].splitlines() if l.startswith("> "))
        after = "\n".join(l[2:] for l in parts[1].splitlines() if l.startswith(">")).replace("**", "")
        out.append((name, before, after.strip()))
    return out


class Examples(unittest.TestCase):
    def test_there_are_6_examples(self):
        self.assertEqual(len(examples()), 6)

    def test_every_after_passes(self):
        for name, _, after in examples():
            with self.subTest(name):
                self.assertTrue(cc.check(after)["ok"], cc.check(after))

    def test_every_before_is_worse(self):
        for name, before, after in examples():
            with self.subTest(name):
                b, a = cc.check(before), cc.check(after)
                self.assertGreater(len(b["problems"]) + len(b["warnings"]), len(a["problems"]) + len(a["warnings"]))


class Rules(unittest.TestCase):
    def test_explaining_phrases_flagged(self):
        r = cc.check("We offer high quality, innovative and seamless service. Book now.")
        self.assertFalse(r["ok"])

    def test_weak_ending_is_a_problem(self):
        r = cc.check("Your roof fixed in 1 day. Feel free to contact us for more information.")
        self.assertTrue(any("weak next step" in p for p in r["problems"]))

    def test_first_line_about_business(self):
        self.assertFalse(cc.check("Welcome to our bakery.\nFresh bread daily.\nOrder on WhatsApp.")["ok"])

    def test_proof_markers_listed(self):
        r = cc.check("Faster invoices.\n[PROOF NEEDED: 1 client quote]\nReply YES.")
        self.assertEqual(r["proof_needed"], ["1 client quote"])

    def test_no_number_warns(self):
        r = cc.check("Your garden, finally tidy.\nCall today.")
        self.assertTrue(any("no number" in w for w in r["warnings"]))

    def test_many_actions_warn(self):
        r = cc.check("Your site in 7 days.\nBook, call, or message us.")
        self.assertTrue(any("several actions" in w for w in r["warnings"]))

    def test_we_vs_you(self):
        r = cc.check("Our team and our tools help us serve 50 clients. Book a call.")
        self.assertTrue(any("'we'" in w for w in r["warnings"]))

    def test_dashes_warn(self):
        r = cc.check("Your site in 7 days — guaranteed. Book a call.")
        self.assertTrue(any("dashes" in w for w in r["warnings"]))

    def test_curly_apostrophe(self):
        self.assertFalse(cc.check("Don’t hesitate to reach out.")["ok"])


class CommandLine(unittest.TestCase):
    def run_cli(self, *args, stdin=None):
        return subprocess.run([sys.executable, SCRIPT, *args], input=stdin, capture_output=True, text=True)

    def test_self_test(self):
        self.assertEqual(self.run_cli("--self-test").returncode, 0)

    def test_exit_code_fail(self):
        self.assertEqual(self.run_cli("--text", "Welcome to ABC. Feel free to contact us.").returncode, 1)

    def test_exit_code_pass(self):
        self.assertEqual(self.run_cli("--text", "Your site in 7 days.\n120 sites built.\nBook a call.").returncode, 0)

    def test_stdin_and_json(self):
        r = self.run_cli("-", "--json", stdin="Your site in 7 days.\n120 built.\nBook a call.")
        self.assertIn('"ok": true', r.stdout)

    def test_missing_file(self):
        self.assertEqual(self.run_cli("does-not-exist.txt").returncode, 2)

    def test_empty_text(self):
        self.assertEqual(self.run_cli("--text", "   ").returncode, 2)


if __name__ == "__main__":
    unittest.main()
