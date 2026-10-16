# Show, Don't Tell

A free AI skill that rewrites your website, sales emails, proposals, DM replies, Google profile or pitch so they **show the result instead of explaining the product**.

**Download:** [latest release (zip)](https://github.com/onittindwani-ai/show-dont-tell-ai-skill/releases/latest) · **Source:** [github.com/onittindwani-ai/show-dont-tell-ai-skill](https://github.com/onittindwani-ai/show-dont-tell-ai-skill)

Works for any business: a dentist, a cafe, an accountant, an agency, a plumber, a software company. No filming, no design skills, no code needed.

## The problem it solves

Most business text explains:

> Welcome to Smile Dental Clinic. We offer high quality dental care with state of the art equipment and a patient first approach. Feel free to contact us for more information.

Nobody remembers that, because every competitor says the same thing. This skill turns it into something people can picture:

> **Walk out with a whiter smile in 1 visit.**
> Before: you hide your teeth in photos. After: you smile without thinking about it.
> 1,200+ patients treated since 2015. "I finally smile in photos again." Neha R., Google review
> **Book a free 15 minute check up.**

(Example business. In real use, only your own facts and proof are used.)

## What it does

1. **Result first.** The first line says what your customer gets, not what your business does.
2. **Before and after.** It shows your customer's life before and after you, in plain words.
3. **Real proof only.** It uses your real numbers, reviews and results. It never invents a number, a review or a client. If you don't have proof yet, it marks the spot `[PROOF NEEDED]` and tells you exactly how to collect it in 2 weeks.
4. **One clear next step.** No more "contact us for more info". One specific action.
5. **Plain words.** It removes phrases like "high quality", "one stop solution", "customer first" and "innovative".
6. **Your facts stay yours.** Same offer, same prices, same tone.

## 3 ways to use it

### 1. Easiest: paste a prompt (ChatGPT, Claude, Gemini, any AI chat)

Open [PASTE-INTO-CHATGPT-OR-CLAUDE.md](PASTE-INTO-CHATGPT-OR-CLAUDE.md), copy the box, paste it into a new chat, then paste your text under it. That's it.

### 2. Claude (claude.ai or the desktop app)

1. Download the zip from the [latest release](https://github.com/onittindwani-ai/show-dont-tell-ai-skill/releases/latest).
2. In Claude, open **Settings, Capabilities, Skills**, and upload the zip. (On plans without Skills: create a Project and paste the prompt file into its instructions.)
3. In any chat, say: "Use show, don't tell on my homepage", and paste your text.

### 3. Claude Code or Codex

```
git clone https://github.com/onittindwani-ai/show-dont-tell-ai-skill.git ~/.claude/skills/show-dont-tell
```

For Codex, clone into `~/.agents/skills/show-dont-tell` instead. Then ask: "Use the show-dont-tell skill on landing-page.html".

## What's in the folder

| File | What it's for |
| --- | --- |
| `SKILL.md` | The skill: the 6 rules, the steps and special situations |
| `PASTE-INTO-CHATGPT-OR-CLAUDE.md` | The no install version: one prompt to copy |
| `templates/` | 6 fill in templates: homepage, sales email, proposal opener, DM reply, Google profile, pitch |
| `references/EXPLAINING-PHRASES.md` | 18 phrases that explain instead of show, and what to write instead |
| `references/PROOF-RULES.md` | What counts as proof, what never to do, and a 2 week plan to collect proof |
| `references/EXAMPLES.md` | 6 full before and after rewrites |
| `scripts/check_copy.py` | An optional checker that flags explaining phrases, weak endings and missing proof |
| `tests/` | 18 automatic tests, run on GitHub for every change |

## Check your text yourself (optional)

If you have Python 3.9 or newer:

```
python scripts/check_copy.py my-homepage.txt
```

It only reads your file. It never changes it and never sends it anywhere.

## Honest limits

- It makes your text clearer and more convincing. It can't create proof you don't have, and it won't fake it.
- Results depend on your offer and your audience. Test the new version against the old one (the skill suggests a simple test every time).
- For health, legal and finance businesses, check final wording with your regulator or lawyer.

## Privacy

Everything runs inside the AI tool you already use. This skill has no server, no tracking and no account. Don't paste passwords, customer personal data or anything confidential into any AI chat.

## Found a problem?

Open an issue on [GitHub](https://github.com/onittindwani-ai/show-dont-tell-ai-skill/issues). Please don't paste private customer details into an issue.

## License

MIT. Free to use, change and share.
