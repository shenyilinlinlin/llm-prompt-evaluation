prompt_v1_minimal = """
Write a function to separate balanced parentheses groups.
"""

prompt_v2_basic_constraints = """
Write a Python function:

def separate_paren_groups(paren_string, remove_unbalanced=False)

Return balanced parentheses groups.
Ignore non-parenthesis characters.
"""

prompt_v3_structured = """
Write a Python function:

def separate_paren_groups(paren_string, remove_unbalanced=False)

Rules:
1. Ignore all characters except '(' and ')'
2. Only return balanced groups
3. Track nesting depth
"""

prompt_v4_final = """
Write a Python function:

def separate_paren_groups(paren_string, remove_unbalanced=False)

Rules:
1. Ignore all non-parenthesis characters
2. Only return OUTERMOST balanced groups
3. A group starts when depth goes 0 -> 1
4. A group ends when depth returns to 0
5. If remove_unbalanced is True:
   - Count unmatched '(' and ')'
   - Ignore incomplete groups
6. If remove_unbalanced is False:
   - return removed_count = 0
"""
