#!/usr/bin/env python3
"""
Auto-generates README.md for the dsa-practice repo by scanning pattern
folders for solved-problem files and cross-referencing them against
problems.json (the master list of every problem in the roadmap).

USAGE:
    Place this script and problems.json in the ROOT of your dsa-practice
    repo (same level as your pattern folders like "Sliding Window/",
    "Trees/", etc). Then run:

        python generate_readme.py

    Re-run it any time after solving new problems and pushing files —
    it regenerates README.md from scratch based on what's on disk.

HOW IT DETECTS "SOLVED" (two strategies, tried in order):
    1. Number-prefix match: file starts with "<problem_number>_" or
       "<problem_number>-" (e.g. "238_Product_of_Array_Except_Self.py"
       matches problem 238). Case-insensitive, ignores leading zeros.
    2. Title-keyword fallback: if no numbered file is found, it compares
       the file's name (with underscores/hyphens treated as spaces) to
       the problem's title, ignoring common stopwords (a, of, the, in...).
       If most of the title's significant words appear in the filename,
       it's counted as solved. This handles files like "path_sum.py"
       matching "Path Sum" even with no LeetCode number in the name.
       Each file can only be credited to ONE problem per run, so it
       won't double-count a single file across two different problems.

    Recommendation: prefix new files with the LeetCode number going
    forward (e.g. "112_Path_Sum.py") — it's the more reliable match and
    removes any ambiguity as your repo grows.

CUSTOMIZING:
    - Add new problems/patterns by editing problems.json.
    - If your folder names differ from what's in problems.json, either
      rename your folders to match, or edit the "folder" field per
      pattern in problems.json.
"""

import json
import os
import re
import sys
from datetime import date

MANIFEST_FILE = "problems.json"
OUTPUT_FILE = "README.md"

STOPWORDS = {
    "a", "an", "the", "of", "in", "is", "to", "and", "or", "from", "with",
    "i", "ii", "iii", "iv", "v", "for", "on", "at", "by", "into"
}

TITLE_MATCH_THRESHOLD = 0.6  # fraction of significant title words that must appear in filename


def normalize_words(text: str) -> set:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if w not in STOPWORDS}


def find_solution_file(folder_path: str, problems: list, used_files: set) -> dict:
    """Given a folder and the list of problems in that pattern, return a
    dict of {problem_number: matched_filename} for every problem solved
    in that folder. Mutates used_files to prevent one file being credited
    to two different problems."""
    matches = {}
    if not os.path.isdir(folder_path):
        return matches

    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Pass 1: number-prefix matching (high confidence, do this first)
    for prob in problems:
        num = prob["number"]
        prefix_pattern = re.compile(rf"^0*{num}[_\-]")
        for f in all_files:
            if f in used_files:
                continue
            if prefix_pattern.match(f):
                matches[prob["number"]] = f
                used_files.add(f)
                break

    # Pass 2: title-keyword fallback for problems still unmatched.
    # Compute ALL candidate (problem, file, score) triples first, then
    # assign highest-scoring pairs globally — prevents a weak early match
    # (e.g. "Diameter of Binary Tree" grabbing a file that's a much better
    # fit for "Binary Tree Right Side View" just because it was checked
    # first) from stealing a file that belongs to a better-fitting problem.
    remaining_problems = [p for p in problems if p["number"] not in matches]
    candidates = []
    for prob in remaining_problems:
        title_words = normalize_words(prob["title"])
        if not title_words:
            continue
        for f in all_files:
            if f in used_files:
                continue
            name_no_ext = os.path.splitext(f)[0]
            file_words = normalize_words(name_no_ext.replace("-", " ").replace("_", " "))
            overlap = title_words & file_words
            score = len(overlap) / len(title_words)
            if score >= TITLE_MATCH_THRESHOLD:
                candidates.append((score, prob["number"], f))

    # Highest-confidence matches win first; ties broken arbitrarily but
    # stably (sort is stable, so original order is the tiebreaker).
    candidates.sort(key=lambda c: c[0], reverse=True)
    matched_problems, matched_files = set(), set()
    for score, prob_number, f in candidates:
        if prob_number in matched_problems or f in used_files:
            continue
        matches[prob_number] = f
        used_files.add(f)
        matched_problems.add(prob_number)

    return matches


def build_pattern_section(pattern: dict, repo_root: str) -> tuple:
    folder_path = os.path.join(repo_root, pattern["folder"])
    used_files: set = set()
    matches = find_solution_file(folder_path, pattern["problems"], used_files)

    lines = [
        f"### {pattern['name']}",
        "| # | Problem | Status |",
        "|---|---------|--------|",
    ]
    solved = 0
    for prob in pattern["problems"]:
        if prob["number"] in matches:
            status = "✅"
            solved += 1
        else:
            status = "⏳ Planned"
        lines.append(f"| {prob['number']} | {prob['title']} | {status} |")

    total = len(pattern["problems"])
    lines.append("")
    return "\n".join(lines), solved, total


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(repo_root, MANIFEST_FILE)

    if not os.path.isfile(manifest_path):
        print(f"ERROR: {MANIFEST_FILE} not found next to this script.")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    sections = []
    total_solved = 0
    total_problems = 0

    for pattern in manifest["patterns"]:
        section_md, solved, total = build_pattern_section(pattern, repo_root)
        sections.append(section_md)
        total_solved += solved
        total_problems += total

    roadmap_lines = "\n".join(f"- [ ] {item}" for item in manifest.get("roadmap_ahead", []))
    pct = round((total_solved / total_problems) * 100) if total_problems else 0

    readme = f"""# DSA Practice — SDE Interview Prep

Pattern-wise Data Structures & Algorithms practice repository, built as part of structured preparation for entry-level SDE roles. All solutions in Python 3.

**LeetCode:** [Daksh_Devyansh](https://leetcode.com/Daksh_Devyansh)

**Progress: {total_solved} / {total_problems} problems solved ({pct}%)**

---

## 📌 Approach

Every problem follows a fixed discipline before code is written:
1. Identify the pattern
2. Justify why the pattern applies
3. State time/space complexity of the intended approach

Then implement, trace through an example, and check edge cases before submitting.

---

## ✅ Progress Tracker


{chr(10).join(sections)}

---

## 🗺️ Roadmap Ahead

{roadmap_lines}

---

## 📁 Structure

Each solved problem lives in its pattern folder. Number-prefixed filenames and the numbers are their leetcode problem numbers.
(e.g. `560_Subarray_Sum_Equals_K.py`) are matched most reliably — recommended
going forward:

```
dsa-practice/
├── Two Pointers/
│   └── 125_Valid_Palindrome.py
├── Sliding Window/
│   └── 3_Longest_Substring_Without_Repeating_Characters.py
├── Prefix Sum_or_Difference Array/
│   └── 560_Subarray_Sum_Equals_K.py
└── ...
```

---

*Last auto-generated: {date.today().isoformat()}*
"""

    output_path = os.path.join(repo_root, OUTPUT_FILE)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"README.md regenerated: {total_solved}/{total_problems} problems marked solved ({pct}%).")


if __name__ == "__main__":
    main()
