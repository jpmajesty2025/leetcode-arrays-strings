# LeetCode — Arrays & Strings

Python solutions to LeetCode array and string problems, each with a corresponding test suite.

## Solutions

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| `merge_sorted_arrays.py` | Merge two sorted arrays into one sorted array | Two pointers | O(n + m) | O(n + m) |
| `is_subsequence.py` | Check if string `s` is a subsequence of string `t` | Two pointers | O(n) | O(1) |
| `in_place_string_reversal.py` | Reverse an array of characters in-place | Two pointers | O(n) | O(1) |

## Project structure

```
.
├── merge_sorted_arrays.py
├── is_subsequence.py
├── in_place_string_reversal.py
├── tests/
│   ├── test_merge_sorted_arrays.py
│   ├── test_is_subsequence.py
│   └── test_in_place_string_reversal.py
├── conftest.py
├── requirements.txt
└── .gitignore
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Running tests

```bash
pytest tests/ -v
```
