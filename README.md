# Lab 6 — The data is the bug

**ECBS5293 — Computing for Analytical Work · Session 3, Block 6**

## Goal

`scripts/load.py` loads customers and orders, keeps paid orders, joins them, and writes revenue per region to `output/revenue_by_region.csv`. When you are done it prints four regions with a number each and a `rows: … missing amounts: …` line.

## How to get it

In your terminal (Git Bash on Windows, Terminal on macOS), in the folder where you keep course work:

```bash
git clone https://github.com/earino/ecbs5293-lab06-data-files.git
cd ecbs5293-lab06-data-files
```

Commands in this lab run in that terminal, from this folder. To edit files (`scripts/load.py`, `DIAGNOSIS.md`, `NEXT_TIME.md`), open **this folder** in VS Code (*File → Open Folder…*; if VS Code asks whether you trust the authors, choose **Yes**).

## Start here

In the terminal, from the project folder — **look at the files first**, then run the script:

```bash
head -5 data/raw/customers.csv
head -5 data/raw/orders.csv
wc -l data/raw/*.csv
uv sync
uv run python scripts/load.py
```

`head -5` prints a file's first five lines; `wc -l` counts its lines. You used both in Session 1. Thirty seconds with them answers most of today's questions before any Python runs. `tail -3` shows the last lines (a footer? a totals row?) and `file` says what kind of file it really is. Ask the file questions like these; do not open it and scroll. That is not inspecting, and on a real export of a million lines it does not work at all.

## What is broken

The code is mostly reasonable and has sanity checks built in. It fails on the first one. Every failure here is a property of the files, not of the code. Fix each with a *loading option* (`sep`, `skiprows`, `na_values`, `thousands`, `pd.to_datetime(...)` and its arguments) or a small cleaning step — **never by editing the data files**. Next month's export arrives the same way, and nobody will be there to edit it.

**Open `DIAGNOSIS.md` before you change the load.** Each fix removes the message that proved the problem before it. When an assertion or a traceback appears, paste its last line into the next note's part 3, with the `head` / `wc -l` / `dtypes` output that shows the cause in the file, then fix, then write the rest.

## What you need to produce

1. The script running with all its assertions passing and the output file written.
2. Validation printed or written: row count, column names, dtypes, missing counts — the four-line sanity check on each dataframe — and the row count compared with `wc -l` minus the lines that are not data.
3. `DIAGNOSIS.md` — one five-part note per data problem you fixed; the file is laid out with a section for each.
4. `NEXT_TIME.md` — "what could break next time": three things about these files that would break this script if the next export changed them, and what check would catch each.
5. **A commit of the working state**, then `git status` clean. In the terminal, from the project folder:

   ```bash
   git status
   git diff
   git add .
   git commit -m "<what you fixed, one line>"
   git status                            # should say: nothing to commit, working tree clean
   ```

   Read the `git diff` before you commit: any debugging `print` you left in the script is in it.
6. **Explain it to a neighbour**, in the last ten minutes (the slide tells you when): symptom, cause, evidence, change, verification, pointing at your screen, not reading the note. Your neighbour asks the three questions on the slide, then you swap. Unsure, or you two disagree? Hands up, and one of us comes to you first.
7. **Lab checkpoint on Moodle**, before you leave: upload the `DIAGNOSIS.md` from your project folder, with its first line filled in (who you explained to, what you need help with).

## Rules

- Fix the *cause*, not the symptom. Do not hard-code a path to your own machine. Never edit `data/raw/`: if you have, `git restore data/raw` puts it back.
- You may use AI to explain errors and suggest what to inspect. You must be able to explain every change you make — your neighbour will ask you to at the end of the lab, in about a minute, without notes, and staff listen in.

## Hints, if stuck

This is a script, so an inspection in Python shows nothing unless you `print(...)` it: put the line right after the load, run the script again with the same command, and read what it printed.

1. `head -3` a file. Count the separators. Count the lines above the real header. Is the first line a header at all?
2. `print(df.dtypes)` after loading. If `amount` says `str` (or `object`, on an older pandas), it is text: `print(df["amount"].head())` — what characters are in there besides digits? Then look at the *rest* of the column: `print(df["amount"].unique())` shows every spelling, including the ones that mean "missing".
3. `print(df["order_date"].head(10))` — is every date written the same way? `pd.to_datetime` has a `format=` argument that names one exact layout (`"%Y-%m-%d"`, `"%d/%m/%Y"`) and an `errors="coerce"` argument that turns what does not match into `NaT` instead of stopping. Two formats in one column means two calls, combined; then count the `NaT`. The error message will suggest `format="mixed"`: that *guesses* a layout per value, and for a date like `2024-01-06` or `04/02/2024` it can guess wrong without telling you. Which slash layout is it, day first or month first? Do not decide on a date like `02/11/2024`, which reads fine both ways; find one whose first number is above 12. If you name the wrong layout, every such date becomes `NaT`, and the count tells you.
4. pandas already treats some spellings as missing (`NA`, `n/a`, an empty cell). `print(df.isna().sum())` before and after `na_values=` tells you whether the spelling in *this* file is one of them.

## Diagnosis note

`DIAGNOSIS.md`, one section per file problem. The evidence here is the file and the dataframe: `head`, `wc -l`, the assertion or traceback line, `dtypes`, `.head()` on the column, `isna().sum()`.

## Stretch task

Write `validate(df, expected_columns, min_rows)` and call it after each load; then write a five-line data-quality report to `output/quality.txt` (rows, missing per column, min/max date, min/max amount, number of regions).

## The last ten minutes

Finished or not, at minute 33 you turn to the person next to you (three if the row is odd). One of you explains, about a minute: what failed, why, the evidence that showed you, what you changed, how you know it works. Point at the screen; do not read the note. The other asks:

1. Show me the evidence — the raw output that told you the cause.
2. Why did it fail, not just where?
3. The what-if question on the slide.

Then swap. If either of you is unsure, or you disagree, put a hand up: staff come to you first. Then the answer to the what-if, for everyone. An unfinished repair is explained the same way — what you found so far.

Before you leave: the lab's **checkpoint on Moodle** — upload the `DIAGNOSIS.md` from your project folder with its first line filled in. That is what "complete" means; nobody signs you off.

## If you got lost: how to reset

Both of these **destroy work**. Read before running.

**Discard uncommitted changes (destructive)** — throw away edits and new files; keep your commits:

```bash
git restore --staged --worktree .    # every tracked file back to the last commit, staged or not
git clean -fd                        # and remove new, untracked files
```

> ⚠️ Permanently deletes uncommitted changes — staged or not — and any new untracked files.

**Full reset to the starter state (destructive)** — back to exactly what you cloned; throws away your commits too:

```bash
git reset --hard origin/main
git clean -fdx
```

> ⚠️ Discards your local commits and uncommitted changes. The `-x` also removes ignored files — `output/`, the `.venv/` environment — so the folder truly matches a fresh clone (`uv sync` rebuilds the environment in a minute). Without `-x`, leftover generated files can hide the very failure the lab wants you to meet again.
