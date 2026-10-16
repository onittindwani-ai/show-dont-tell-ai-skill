---
name: show-dont-tell
description: Rewrite any business text so it shows the result instead of explaining the product. Use when someone pastes a website homepage, a sales email, a proposal, a WhatsApp or DM reply, a Google Business profile, a pitch, an ad or any text that describes a business, or asks to make their copy, page, email or pitch more convincing. Leads with the result, adds a before and after, uses only real proof, and ends with one clear next step.
license: MIT
metadata:
  version: "1.0.0"
  works-with: "ChatGPT, Claude, Claude Code, Codex, Gemini"
---

# Show, Don't Tell

Most business text explains: "We offer high quality services with a customer first approach." Nobody remembers that. People remember what they can see: a result, a change, a number, a real customer.

Your job: take the person's text and rewrite it so a stranger understands, in about 5 seconds, what changes for them, why they should believe it, and what to do next.

## The 6 rules (never break these)

1. **Result first.** The first line says what the customer gets, in their words, not what the business does. "Your website, live in 7 days" beats "We are a full service web design agency".
2. **Before and after.** Show the customer's life before and after, in 1 or 2 short lines each. Concrete and physical: hours, money, worry, a specific moment.
3. **Real proof only.** Use only proof the person gave you or that is already in their text: a number, a review, a client result, a count, a guarantee they really offer. Never invent a number, a review, a client, a rating or a guarantee. If there is no proof, write `[PROOF NEEDED: what to collect]` in that spot and tell them how to get it. See [references/PROOF-RULES.md](references/PROOF-RULES.md).
4. **One clear next step.** End with exactly one action, specific and easy ("Book a free 15 minute call", "Reply YES and I'll send the quote"). Never "contact us for more info", never 3 buttons.
5. **Plain words.** Short sentences. Everyday words a 12 year old knows. Cut the explaining phrases listed in [references/EXPLAINING-PHRASES.md](references/EXPLAINING-PHRASES.md).
6. **Keep it true and theirs.** Keep their facts, prices, names and offer. Do not add services they don't sell. Keep the length close to the original unless they ask for shorter or longer. Match their tone (friendly, formal, local).

## How to work

1. **Ask what it is, if it's not obvious.** One short question: "Is this your homepage, a sales email, a proposal, a DM reply, your Google profile, or a pitch?" If it's obvious, don't ask.
2. **Find the explaining lines.** List every line that describes the business instead of showing a result. Quote them.
3. **Collect the proof.** Pull every real number, review and result already in the text. If there is none, ask once: "Do you have any of these: a number (clients, years, results), a short customer review, or a before and after? Paste anything you have." If they have nothing, continue and leave `[PROOF NEEDED: ...]` markers.
4. **Rewrite** with the matching template in [templates/](templates/): homepage, sales email, proposal opener, DM reply, Google profile, or pitch.
5. **Check yourself** with the list below. If you can run code, run `python scripts/check_copy.py yourfile.txt`.
6. **Reply in this order:**
   - **The new version**, ready to paste.
   - **What changed**, in 3 bullets or fewer.
   - **Proof to collect**, only if you left `[PROOF NEEDED]` markers.
   - **One test to try** (for example: "Send the new email to 10 people and the old one to 10 people. Count replies after 3 days.").

## Check before you send

- [ ] The first line is a result for the customer, not a description of the business.
- [ ] There is a before and an after.
- [ ] Every number, review, client and guarantee came from the person. Nothing was invented.
- [ ] Missing proof is marked `[PROOF NEEDED: ...]`, not faked.
- [ ] Exactly one next step at the end.
- [ ] None of the explaining phrases are left ("we offer", "high quality", "one stop solution", "customer first", "passionate about"...).
- [ ] Same offer, same prices, same facts as the original.

## Special situations

- **They want it shorter or longer:** keep all 6 rules; change only the length.
- **Regulated business** (health, legal, finance): never promise outcomes ("guaranteed results", "cure", "you will win"). Show the process and real, allowed proof instead. Add a note telling them to check the wording with their regulator or lawyer.
- **No proof at all:** don't stall. Write the strongest honest version, use specific details of the process as proof ("You get a written quote within 24 hours"), and list exactly what proof to collect over the next 2 weeks.
- **Many pieces at once:** do them one at a time, homepage first, and ask before doing the rest.
- **They ask for fake reviews or made up numbers:** refuse that part in one sentence, explain it can break consumer protection law and platform rules, and offer the honest version.

## Examples

See [references/EXAMPLES.md](references/EXAMPLES.md): 6 full before and after rewrites (dentist, accountant, cafe, marketing agency, software tool, home repair).
