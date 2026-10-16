#!/usr/bin/env python3
"""Check business text for "explaining" instead of "showing".

Read only: it never changes your file. No dependencies (Python 3.9 or newer).

Usage:
  python scripts/check_copy.py page.txt          check a file
  python scripts/check_copy.py --text "..."       check some text
  cat page.txt | python scripts/check_copy.py -   check text from stdin
  python scripts/check_copy.py page.txt --json    machine readable result
  python scripts/check_copy.py --self-test        run the built in tests

Exit code: 0 when there are no problems, 1 when a problem is found, 2 for a usage error.
Warnings are suggestions; problems are things the method says must be fixed.
"""
import argparse
import json
import re
import sys

EXPLAINING = [
    "we offer", "we provide", "high quality", "best in class", "world class", "industry leading", "leading provider",
    "one stop", "end to end", "customer first", "customer centric", "passionate about", "innovative", "cutting edge",
    "next generation", "state of the art", "tailored solutions", "bespoke solutions", "customised solutions",
    "customized solutions", "seamless", "hassle free", "trusted by many", "competitive prices", "affordable prices",
    "wide range of", "solutions for", "leverage", "synergy", "empower", "we are a", "welcome to",
]
WEAK_ENDINGS = [
    "contact us for more", "feel free to", "don't hesitate", "do not hesitate", "for more information",
    "get in touch for more", "let us know if you have any questions", "share your requirement",
]
ACTION_WORDS = ["book", "call", "reply", "order", "buy", "sign up", "subscribe", "visit", "download", "message",
                "whatsapp", "schedule", "register", "click", "send", "show", "try", "start", "scan", "walk in", "pick"]
DASHES = "‒–—―"


def _lower(text):
    return text.lower().replace("’", "'")


def check(text):
    """Return a dict with problems, warnings and facts about the text."""
    low = _lower(text)
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    first = _lower(lines[0]) if lines else ""
    words = re.findall(r"[A-Za-z0-9']+", text)
    problems, warnings = [], []

    found = sorted({p for p in EXPLAINING if p in low})
    if found:
        warnings.append("explaining phrases: " + ", ".join(found))
    if len(found) >= 3:
        problems.append("3 or more explaining phrases: the text describes the business instead of showing a result")

    if re.match(r"^(welcome|we |we're|we are|our |at [a-z]+ we|hello,? we)", first):
        problems.append("the first line is about the business, not the customer's result")

    weak = sorted({p for p in WEAK_ENDINGS if p in low})
    if weak:
        problems.append("weak next step: " + ", ".join(weak) + " (end with one specific action)")

    last = _lower(lines[-1]) if lines else ""
    actions = sorted({a for a in ACTION_WORDS if re.search(r"\b" + re.escape(a) + r"\b", last)})
    if not actions and not weak:
        warnings.append("no clear next step found in the last line")
    if len(actions) >= 3:
        warnings.append("the last line asks for several actions (" + ", ".join(actions) + "): keep one")

    if not re.search(r"\d", text) and "[proof needed" not in low:
        warnings.append("no number or proof marker: add a real number, review or result, or a [PROOF NEEDED: ...] marker")

    we = len(re.findall(r"\b(we|our|us)\b", low))
    you = len(re.findall(r"\b(you|your|you're)\b", low))
    if we > you:
        warnings.append("talks about 'we' (%d) more than 'you' (%d)" % (we, you))

    if any(d in text for d in DASHES):
        warnings.append("long dashes found: use commas or full stops")

    markers = re.findall(r"\[PROOF NEEDED:([^\]]*)\]", text, flags=re.I)
    return {
        "ok": not problems,
        "problems": problems,
        "warnings": warnings,
        "proof_needed": [m.strip() for m in markers],
        "words": len(words),
        "we_count": we,
        "you_count": you,
    }


def report(result):
    out = []
    out.append("PASS" if result["ok"] else "FIX NEEDED")
    for p in result["problems"]:
        out.append("  problem: " + p)
    for w in result["warnings"]:
        out.append("  warning: " + w)
    for m in result["proof_needed"]:
        out.append("  proof to collect: " + m)
    out.append("  words: %d, 'we' %d, 'you' %d" % (result["words"], result["we_count"], result["you_count"]))
    return "\n".join(out)


SELF_TESTS = [
    ("explaining homepage fails",
     "Welcome to ABC. We offer high quality, innovative solutions. Feel free to contact us for more information.", False),
    ("showing homepage passes",
     "Your website, live in 7 days.\nBefore: no site. After: customers find you on Google.\n120 sites built since 2019.\nBook a free 15 minute call.", True),
    ("weak ending fails", "Your books, done every month. Don't hesitate to reach out.", False),
    ("first line about us fails", "We are a leading agency.\nYou get more calls.\nBook a call.", False),
    ("proof marker counts as proof", "Fresh bread every morning.\n[PROOF NEEDED: a review]\nOrder on WhatsApp.", True),
    ("plain DM reply passes", "Hi! A leaking tap fix is 400 to 700 rupees. Send me a photo and I'll give you the exact price.", True),
]


def self_test():
    failed = 0
    for name, text, want_ok in SELF_TESTS:
        got = check(text)["ok"]
        status = "ok  " if got == want_ok else "FAIL"
        if got != want_ok:
            failed += 1
        print("%s  %s" % (status, name))
    print("%d of %d self tests passed" % (len(SELF_TESTS) - failed, len(SELF_TESTS)))
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check business text for explaining instead of showing.")
    ap.add_argument("file", nargs="?", help="a text file, or - for stdin")
    ap.add_argument("--text", help="check this text instead of a file")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--self-test", action="store_true", help="run the built in tests")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if a.text is not None:
        text = a.text
    elif a.file == "-":
        text = sys.stdin.read()
    elif a.file:
        try:
            with open(a.file, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print("could not read the file: %s" % exc, file=sys.stderr)
            return 2
    else:
        ap.print_usage(sys.stderr)
        return 2
    if not text.strip():
        print("the text is empty", file=sys.stderr)
        return 2
    result = check(text)
    print(json.dumps(result, indent=2) if a.json else report(result))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
