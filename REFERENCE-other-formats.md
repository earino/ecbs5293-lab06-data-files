# Reference: other formats and other problems

Not lectured — Block 6 is CSV only. Keep this for the stretch task and for the first time one of these bites you.

## Excel files

`pd.read_excel("file.xlsx", sheet_name="Sheet1")` needs the `openpyxl` package (`uv add openpyxl`). Risks: hidden sheets, merged cells, numbers stored as text with a leading apostrophe, dates that Excel silently converted (`1/2/2024` — January 2nd or February 1st?), and **opening a CSV in Excel and saving it**, which can rewrite delimiters, quote characters, and dates. Never round-trip course data through Excel.

## JSON

```python
import json
with open("data/raw/orders.json", encoding="utf-8") as fh:
    records = json.load(fh)          # a list of dicts, usually
df = pd.DataFrame(records)           # or pd.json_normalize(records) for nested fields
```

Malformed JSON raises `json.JSONDecodeError` with a line and column — read them. Common causes: a trailing comma, single quotes, one JSON object per line (that is "JSON Lines": `pd.read_json(path, lines=True)`).

## Encodings

A file is bytes; an encoding says how to turn them into text. `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9` means the file is not UTF-8 — often `latin-1` / `cp1252` from an older Windows export. Inspect with `file data/raw/x.csv`, which names the file's type and, for text, its encoding (it works in Git Bash as well as on macOS; `head -c 300 data/raw/x.csv` shows the raw start of the file too); load with `pd.read_csv(path, encoding="latin-1")`. Names like *Kovács* turning into *KovÃ¡cs* is the same problem in the other direction.

## File size and memory

`ls -lh data/raw/` before loading. A 2 GB CSV will not open in Excel at all and may not fit in memory as a dataframe. Options, in order: load only the columns you need (`usecols=`), load a sample (`nrows=100000`) to design the pipeline, then process in chunks (`chunksize=`). `wc -l` tells you how many rows you are facing before you commit to anything.

## Why Excel is misleading on large files

Excel shows at most ~1,048,576 rows and says nothing when a file has more. It also formats numbers for display (`1,200` vs `1200`) and guesses types per cell. What you see in Excel is not what is in the file. `head`, `wc -l`, and `df.dtypes` are.
