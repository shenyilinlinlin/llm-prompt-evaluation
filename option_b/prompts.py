prompt_v1_minimal = """
Write a function starts_one_ends(n, x, y).

Return the number of n-digit positive integers that:
start with digit x OR end with digit y.
"""

prompt_v2_basic_constraints = """
Write a Python function starts_one_ends(n, x, y).

Task:
Count numbers that satisfy:
- first digit is x OR
- last digit is y

Return the total count as integer.

If no valid numbers exist, return -1.
"""

prompt_v3_structured = """
Write a Python function starts_one_ends(n, x, y).

Definition:
Return count of n-digit integers where:
- first digit == x OR last digit == y

Constraints:
- n is up to 5
- x and y are digits 0-9

Important:
- A number satisfying both conditions should only be counted once
- Handle overlap cases explicitly
- Avoid double counting
"""

new_stmt = """
Write a Python function: def starts_one_ends(n, x, y)
You are given three integers n, x, y.

Your task is to return the number of n-digit integers such that:
- the first digit is x OR
- the last digit is y

Rules:
1. Valid inputs:
   - 1 <= n <= 5
   - 0 <= x <= 9
   - 0 <= y <= 9
2. Number definition:
   - For n > 1, numbers cannot start with 0
   - For n = 1, valid numbers are 0 through 9
3. Counting rule:
   - Count numbers satisfying (first digit == x) OR (last digit == y)
   - Each number must be counted only once (no double counting overlap)
4. Edge cases:
   - Handle x == 0 correctly (no valid multi-digit numbers start with 0)
   - Handle y == 0 normally (ending with 0 is valid)
   - Handle n == 1 separately
5. Invalid input:
   - Return -1 if n is outside [1,5]
   - Return -1 if x or y is outside [0,9]
6. Output:
   - Return only the integer result
"""
