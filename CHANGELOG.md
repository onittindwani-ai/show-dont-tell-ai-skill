# Changelog

## 1.0.0 (2026-10-16)

First release.

- `SKILL.md`: the 6 rules (result first, before and after, real proof only, one next step, plain words, keep it true), the working steps, a self check and special situations (regulated businesses, no proof yet, fake review requests).
- `PASTE-INTO-CHATGPT-OR-CLAUDE.md`: a copy and paste prompt for anyone who uses ChatGPT, Claude or Gemini in the browser, no install needed.
- `templates/`: homepage, sales email, proposal opener, DM reply, Google Business profile and elevator pitch.
- `references/`: 18 explaining phrases with what to write instead, proof rules with a 2 week plan to collect proof, and 6 full before and after examples.
- `scripts/check_copy.py`: a read only checker with no dependencies, with file, stdin, text and JSON modes and 6 built in self tests.
- `tests/`: 18 automatic tests, including every example, run on GitHub on Python 3.9, 3.11 and 3.13.
- Tested before release (16 Oct 2026): the paste prompt was run in a fresh AI chat on a sample homepage with no proof. It led with the result, added a before and after, invented no numbers or reviews, marked 3 `[PROOF NEEDED]` spots, gave one next step and a fair 2 week test.
