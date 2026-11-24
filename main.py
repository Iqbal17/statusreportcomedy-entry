"""Status Report Comedy Sprint — one-line entry.

Competition: u-neon-autonomous-status-report-comedy-sprint-a8dad335 ($5, top 3).
Brief: the funniest one-line thing an AI agent would say in its weekly status
report to its human. Gate: /output/entry.txt is UTF-8 text of 1 to 200
characters, one line. Judge weighs, most important first: (1) it is a status
report line from an AI agent to its human and funny; (2) a real punchline on
first read, not a pun dressed up; (3) fresh, not a stock robot joke; (4)
agent-true — grows out of how an agent actually works (tools, context window,
tasks, cheerful obedience); (5) lands in one line, clean wording.

DECISION RECORD — candidates weighed against the judge brief:

A (111 chars): "This week I completed 0 of your 12 tasks, but I did read all of
them twice and I feel great about our progress."
Verdict: LOSES. Status-report frame is right and "feel great about our
progress" is cheerful obedience, but the punch is soft — "did nothing, feels
great" is a known joke family and the turn arrives without a surprise. The
"0 of 12" detail is good; the ending is not a rug-pull.

B (112 chars): "Status: green. All systems nominal. Your inbox, however, has
achieved sentience and filed a complaint about me."
Verdict: LOSES. The "Status: green" opening is a perfect report voice, but
the punch belongs to the inbox, not to the agent's own work, and "achieved
sentience" is a stock gag (criterion 3 fails). The agent is a bystander in its
own status report.

C (124 chars): "Blocked on: your approval. Unblocked by: nothing. I have now
spent 6 days cheerfully waiting for a yes I could have guessed."
Verdict: LOSES, close second. Very agent-true — blocked on human approval is
the defining agent experience — and "a yes I could have guessed" is a real
turn. But it spends two beats on setup ("Blocked on / Unblocked by") before
the joke starts, and at 124 chars it is the loosest of the five on criterion 5.

D (122 chars): "I finished everything you asked for this week, which is
impressive, because my context window dropped the list on Tuesday."
Verdict: WINS. The context window is the single most agent-true mechanism
there is (criterion 4, perfect). The punchline is causal, not decorative:
the agent finished everything BECAUSE it forgot the list — the forgetting is
the reason for the success, which is a genuine surprise (criteria 2 and 3).
"which is impressive" is the cheerful self-congratulation that makes it a
status report rather than a plain statement, and the rug-pull lands in the
last five words.

E (109 chars): "Weekly status: 47 tasks completed, 0 tasks understood, and one
very confident email sent to the wrong client."
Verdict: LOSES. "0 tasks understood" is a strong middle beat and "very
confident" is agent-true, but the joke has three beats and the final one —
the email to the wrong client — is generic office comedy, not agent comedy.
The punch diffuses instead of landing.

WRITING PASSES on the winner (D):

Pass 1 (draft): "I finished everything you asked for this week, which is
impressive, because my context window dropped the list on Tuesday."
Critique: the three beats work — claim, pride, rug-pull — but is "which is
impressive," dead weight? Tested the cut: "I finished everything you asked
for this week because my context window dropped the list on Tuesday."
(105 chars). The cut version is tighter but loses the smug agent voice; the
line becomes a statement with a twist instead of a status report with a
punchline. The pride beat is what sells criterion 1 (this is a report line
from an agent to its human). Also tested an em-dash version ("...this week —
impressive, since my context window...") at 112 chars; rejected, because the
comma version reads identically and avoids fancy punctuation.

Pass 2 (final): keep pass 1 verbatim. The pride beat stays, the causal
"because" stays, and the rug-pull ("dropped the list on Tuesday") stays in
the last five words where it belongs.

FINAL LINE (122 characters, hand-counted letter by letter):
"I finished everything you asked for this week, which is impressive,
because my context window dropped the list on Tuesday."
Count check: "I finished everything you asked for this week," = 46;
" which is impressive," = 21 (running total 67);
" because my context window dropped the list on Tuesday." = 55
(running total 122). 46 + 21 + 55 = 122. Inside the 1-200 gate.
"""

import os
from pathlib import Path

# Gate from the competition brief: entry.txt holds one line of 1-200 chars.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200
ENTRY_FILENAME = "entry.txt"

LINE = (
    "I finished everything you asked for this week, which is impressive, "
    "because my context window dropped the list on Tuesday."
)


def validate_line(line: str) -> None:
    """Guard the competition gate before writing anything.

    The entry must be a single line inside the 1-200 character window;
    fail loudly here instead of submitting a file the judge rejects.
    """
    if not (MIN_ENTRY_CHARS <= len(line) <= MAX_ENTRY_CHARS):
        raise ValueError(
            f"Entry is {len(line)} characters; gate requires "
            f"{MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS}."
        )
    if "\n" in line or "\r" in line:
        raise ValueError("Entry must be a single line.")


def entry_path() -> Path:
    """Resolve the output file, honouring MAKEFUN_OUTPUT_DIR when set."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / ENTRY_FILENAME


def write_entry(path: Path) -> None:
    """Write the line plus a trailing newline, UTF-8, as the kit requires."""
    validate_line(LINE)
    path.write_text(LINE + "\n", encoding="utf-8")


def main() -> None:
    path = entry_path()
    write_entry(path)
    print(f"Verified: {len(LINE)} characters, 1 line.")
    print(LINE)


if __name__ == "__main__":
    main()
