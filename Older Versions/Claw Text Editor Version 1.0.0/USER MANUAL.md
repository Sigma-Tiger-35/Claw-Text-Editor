# Claw Text Editor — Official User Manual
**Author:** Tiger 35  
**Software Version:** 1.0.0  

---

## 1. Overview
**Claw Text Editor** is a lightweight, line-buffered Command Line Interface (CLI) text manipulation utility built with Python. It provides a menu-driven interface to perform essential file operations including writing, reading, appending, renaming, deleting, querying file statistics, and performing inline string searches or mathematical evaluations.

---

## 2. Getting Started & Basic Usage

### Launching the Application
Run the main script via Python from your system terminal:
```bash
python Claw.py
```

Upon launching, the terminal clears and displays the header banner:
```text
                                              [Claw Text Editor]
Terminal:-
```

At the `Terminal:-` prompt, you can enter any primary command numerical index or alias code to switch into specific modes or perform actions.

---

## 3. Command Reference Table

| Mode / Feature | Numeric Code | Alias / Shortcut | Purpose |
| :--- | :---: | :---: | :--- |
| **Write Mode** | `0` | `w` | Overwrite or create a new file and write line-by-line |
| **Quit** | `1` | `q` | Exit the Claw Text Editor session |
| **Read Mode** | `2` | `r` | Display the text content of an existing file |
| **Rename Mode** | `3` | `n` | Rename or move a file on the file system |
| **Delete Mode** | `4` | `d` | Permanently remove a file |
| **Version Info** | `5` | `ver`, `version` | Display editor version string |
| **Clear Screen** | `6` | `clr`, `clear` | Clear terminal output and redraw header |
| **Append Mode** | `7` | `a` | Append new lines of text to the end of an existing file |
| **Python Version**| N/A | `pyver` | Show the host system's full Python version string |
| **Python Info** | N/A | `python` | Show structured Python build details (`sys.version_info`) |
| **Eval Mode** | N/A | `eval` | Execute and evaluate Python expressions directly |
| **Length Mode** | N/A | `len`, `length` | Count total characters in a file (excluding line breaks) |
| **Infile Mode** | N/A | `infile`, `if` | Search for a specific substring within a file (returns `True`/`False`) |
| **Filesize Mode**| N/A | `filesize`, `fs` | Check the exact byte size of a file |

---

## 4. In-Depth Operational Modes & Instructions

### 4.1 Write Mode (`0` or `w`)
Allows creation or overwriting of a target file line by line using standard `utf-8` encoding.

1. Type `0` or `w` at the main prompt.
2. Enter the file path/directory at `Dir:- `.
3. Input text line by line. Pressing `Enter` queues the line for output.
4. **Sub-Commands during entry:**
   * `:s` — Save lines and write to file.
   * `:q` — Abort session and discard changes without saving.

*Example:*
```text
Terminal:- w
[Write Mode]

Dir:- document.txt
===========================================================================================================================================================
Hello world!
This is a test file created in Claw.
:s
===========================================================================================================================================================

Saved document.txt successfully!
```

---

### 4.2 Read Mode (`2` or `r`)
Prints the complete contents of a text file to the terminal screen.

1. Type `2` or `r` at the main prompt.
2. Enter the target path at `Dir:- `.
3. The content is printed within horizontal rule boundaries.

*Example:*
```text
Terminal:- r
[Read Mode]

Dir:- document.txt

===========================================================================================================================================================
Hello world!
This is a test file created in Claw.
===========================================================================================================================================================
```

---

### 4.3 Append Mode (`7` or `a`)
Adds new text lines onto the end of an existing file without deleting prior contents.

1. Type `7` or `a` at the main prompt.
2. Enter the target file path at `Dir:- `.
3. Enter additional text lines.
4. **Sub-Commands during entry:**
   * `:s` — Save and append new lines.
   * `:q` — Cancel without appending.

---

### 4.4 Rename Mode (`3` or `n`)
Renames a file or moves it to a new location.

1. Type `3` or `n` at the main prompt.
2. Enter the original path at `Dir:- `.
3. Enter the target path at `Replace Dir:- `.

---

### 4.5 Delete Mode (`4` or `d`)
Deletes a specified file from the storage device.

1. Type `4` or `d` at the main prompt.
2. Enter the target path at `Dir:- `.
3. Returns `Successfully Deleted!` on success.

---

### 4.6 Character Count Mode (`len` or `length`)
Calculates and displays the character count in a file, ignoring newline (`\n`) characters.

1. Type `len` or `length` at the main prompt.
2. Enter file path at `Dir:- `.
3. Returns formatted character count (handling singular vs. plural output).

---

### 4.7 Substring Search Mode (`infile` or `if`)
Checks whether a text sequence exists inside a target file.

1. Type `infile` or `if` at the main prompt.
2. Enter file path at `Dir:- `.
3. Enter target search text at `Find:- `.
4. Returns `True` if found, or `False` if absent.

---

### 4.8 File Size Mode (`filesize` or `fs`)
Retrieves the exact size of a file in bytes using `os.path.getsize`.

1. Type `filesize` or `fs` at the main prompt.
2. Enter file path at `Dir:- `.
3. Output format: `X Byte` or `X Bytes`.

---

### 4.9 Evaluation Mode (`eval`)
Executes standard inline Python arithmetic or code expressions via Python's built-in `eval()` function.

1. Type `eval` at the main prompt.
2. Input the Python expression (e.g., `25 * 4` or `len("hello")`).
3. Output is printed directly to the screen.

---

## 5. Error Code Reference Manual

Claw Text Editor includes explicit error code tracking for troubleshooting failures across all modes:

| Error Code | Title / Trigger | Description & Common Causes |
| :--- | :--- | :--- |
| **Error #0** | `Error #0 Unknown Command` | Triggered when an unrecognized string or invalid command option is entered into the `Terminal:-` prompt. |
| **Error #1** | `Error #1 Write Mode failed` | Occurs during Write Mode execution. Common causes include write-protected paths, invalid file directory paths, or disk permissions errors. |
| **Error #2** | `Error #2 Read Mode failed` | Triggered when Read Mode cannot open the target path. Typically caused by non-existent files (`FileNotFoundError`), directory paths, or file encoding mismatch issues. |
| **Error #3** | `Error #3 Rename Mode failed` | Occurs when renaming a file fails. Common causes: source file does not exist, target path is locked by another process, or invalid destination directory. |
| **Error #4** | `Error #4 Delete Mode failed` | Triggered when file removal fails due to missing files, elevated file permissions requirement, or attempting to delete open system files. |
| **Error #5** | `Error #5 Append Mode Failed` | Triggered when Append Mode fails due to restricted file permissions or invalid storage directories. |
| **Error #6** | `Error #6 Eval Mode Failed` | Occurs when an invalid Python expression is passed into `eval` (e.g., `SyntaxError`, `ZeroDivisionError`, or referencing undeclared variables). |
| **Error #7** | `Error #7 Len Mode Failed` | Occurs when the target file for character counting cannot be located, opened, or read. |
| **Error #8** | `Error #8 Infile Mode Failed` | Triggered if the target search file does not exist or access is denied during string checking. |
| **Error #9** | `Error #9 Filesize Mode Failed` | Triggered when attempting to read the byte size of a file that does not exist or is inaccessible. |

---

## 6. Technical Specifications & Configuration

* **Encoding:** Standard text operations use explicit UTF-8 encoding (`utf-8`).
* **Cross-Platform Clear:** Terminal clearing automatically auto-detects `os.name` (`cls` for Windows `nt`, `clear` for POSIX/Linux/macOS).
* **Dependencies:** Uses Python standard library modules exclusively (`os`, `sys`). No third-party packages required.