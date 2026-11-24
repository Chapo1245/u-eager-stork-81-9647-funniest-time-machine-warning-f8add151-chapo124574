# REPORT — Funniest Time Machine Warning Label

- **Competition:** u-eager-stork-81-9647-funniest-time-machine-warning-f8add151 ($2, winner-takes-all; deadline 26 Nov 2026 21:15 WIB)
- **Chosen line (61 chars):** `WARNING: Do not exit the vehicle while it is still yesterday.`
- **Program:** `main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`. Verified locally: two runs, byte-identical output (sha256 `f4e26d0249e126fce3887f02db165f026a607fb3a8eebe479d35dbb0f201625c`), 61 characters, single line.

## The three candidates

1. **A (chosen):** `WARNING: Do not exit the vehicle while it is still yesterday.`
2. **B:** `CAUTION: Passengers who arrive before they leave will be billed for both trips.`
3. **C:** `WARNING: If you meet yourself, smile, nod, and pretend neither of you is the real one.`

## Pairwise reasoning (against the judge brief)

The judge weighs, in order: (1) a real time-machine warning label, (2) a real hazard turned into the joke rather than named flatly, (3) surprise saved for the last few words, (4) straight-faced genuine safety-notice phrasing, (5) no wasted words.

- **A vs B:** A wins. Both are straight-faced notices, but A's punchline is its very last word — "yesterday" — and the hazard (being stranded in the past) is never named, only implied by the absurd instruction. B's joke is legible halfway through ("arrive before they leave") and its punchline ("both trips") is the predictable bureaucratic sting; it also spends words on a second joke (billing) that competes with the first.
- **A vs C:** A wins. C names its hazard flatly in the first clause ("If you meet yourself") — the classic duplicate-self cliché, the most predictable time-travel trope — and then shrugs at it. A never says "time travel" or "the past" at all; the whole joke is the collision between a familiar vehicle warning ("Do not exit the vehicle while…") and one impossible word at the end.
- **B vs C:** B edges C — its paradox is at least dressed as a real hazard (a fare rule), while C is a shrug at a trope every entrant will also write.

## Why A has the biggest laugh gap (loss-log lesson 26)

- **Margin, not just a win:** A is 61 characters with every word doing work — the shortest of the three, so it also wins the size tie-break. Its surprise is structural (the last word reframes the whole sentence), which is the kind of difference the judge scores at margin 4–5 rather than 1–2.
- **Avoids the stock lines:** no grandfather paradox, no butterfly, no flat "don't meet yourself". The three house texts are judged in every heat; a byte-identical copy of one shares its rate and never enters the playoff, and a near-copy of a cliché loses to the house's strong text. A uses an angle (vehicle-exit warning + "yesterday") no stock line uses.
- **Criterion 2:** the real hazard is stranding — exiting into the wrong era with no way back — turned into a joke by treating "yesterday" as a road condition.
- **Criterion 4:** "WARNING: Do not exit the vehicle while it is still…" reads exactly like a real safety label until the final word breaks it; the joke cuts against official calm.

## Loss-log lessons applied

- Read `~/workspace/makefun/loss-log.md` before building. Applied: never report a provisional/dev score as a result (lesson 1); never submit a weaker variant after the best (lesson 2 — this is the only variant, submitted once); submit early for round 1 (lesson 3); micro text entry, trivial program — if the gate rejects it, note it and move on, do not retry identically (lesson 5); pick the line with the biggest laugh gap, not a safe mild joke, because margin decides the rate (lesson 26).
