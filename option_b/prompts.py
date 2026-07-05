original_prompt = """
Count numbers that start or end with digits.
"""

improved_prompt = """
Write a Python function:

def starts_one_ends(n, x, y)

Rules:
- n in [1,5]
- x, y in [0,9]
- x = 0 is valid
- y = 0 is valid
- Count numbers starting with x OR ending with y
- Avoid double counting overlaps
- Handle n = 1 correctly
"""
