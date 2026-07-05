original_prompt = """
Write a Python function:

def separate_paren_groups(paren_string, remove_unbalanced=False)

Return balanced parentheses groups.
"""

improved_prompt = """
Write a Python function:

def separate_paren_groups(paren_string, remove_unbalanced=False)

Rules:
1. Ignore all non-parenthesis characters
2. Only return OUTERMOST balanced groups
3. Do NOT return nested groups separately
4. A group starts when depth goes from 0 to 1
5. A group ends when depth returns to 0
6. If remove_unbalanced is True:
   - Count unmatched '(' and ')'
   - Do not include incomplete groups
7. If remove_unbalanced is False:
   - Return 0 as removed_count
8. Clean non-parenthesis characters from output
"""
