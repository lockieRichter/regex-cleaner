# Regex Cleaner

This is a simple python package that can be used to clean a verbose regex pattern of the comments and new lines and return the basic underlying pattern.

## Installation

pip install regex_cleaner

## Examples

```python
pattern = """
    This is a verbose regex #With comments.
"""
cleaned_regex = clean_regex(pattern)
```
gives
```
cleaned_regex = "This is a verbose regex"
```
