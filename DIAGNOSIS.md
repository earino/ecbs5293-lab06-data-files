# Diagnosis notes

**One five-part note per data problem**, in the order you met them. The file is laid out with a
section per problem. That is the default shape, not a rule: any organisation that gives every
cause its own evidence is fine, and two problems in the same column may share a note if it
names both.

**Explained to:** ______ · **Need help with:** ______ (write *nothing* if none). This line is your Moodle checkpoint.

**Open this file before you change the load.** Each fix removes the message that proved the
problem before it. When an assertion or a traceback appears, paste its last line into the next
note's part 3, together with what showed the cause *in the file* — `head -5`, `wc -l`,
`df.dtypes`, `df["…"].head()`, `df.isna().sum()` — then fix, then write the rest.

The evidence in this lab is the file and the dataframe. You will not need `pwd`, `os.getcwd()`
or `sys.executable` here; you will need what pandas printed and what the file contains.

---

## Problem 1 — file: ______

1. **What was the symptom?** (What did the script print, or what did the four-line check show?)

2. **What was the actual cause?** (What about the *file* did the code not expect?)

3. **What evidence showed that?** Paste the last line of the assertion or traceback, then the
   file evidence (`head`, `wc -l`) and the dataframe evidence (`dtypes`, `.head()`, `isna().sum()`)
   — raw, not described.

```text

```

4. **What did you change?** (Which loading option or cleaning step — and why that one and not an edit to the file.)

5. **How did you verify it worked?** (Which of the four lines changed, from what to what — `shape`, `dtypes`, `head()`, `isna().sum()` — and does the row count match `wc -l` minus the non-data lines?)

---

## Problem 2 — file: ______

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

```text

```

4. **What did you change?**

5. **How did you verify it worked?**

---

## Problem 3 — file: ______

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

```text

```

4. **What did you change?**

5. **How did you verify it worked?**

---

## Problem 4 — file: ______

1. **What was the symptom?**

2. **What was the actual cause?**

3. **What evidence showed that?**

```text

```

4. **What did you change?**

5. **How did you verify it worked?**
