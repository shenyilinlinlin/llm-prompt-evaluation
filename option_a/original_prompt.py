from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool = False) -> Tuple[List[str], int]:
    result = []
    removed_count = 0
    current_group = []
    balance = 0
    is_unbalanced = False

    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)

        elif char == ')':
            balance -= 1
            current_group.append(char)

            if balance < 0:
                is_unbalanced = True

            if balance == 0 and len(current_group) > 0:
                if not is_unbalanced:
                    result.append("".join(current_group))
                else:
                    if remove_unbalanced:
                        removed_count += 1

                current_group = []
                is_unbalanced = False

    if balance != 0 and remove_unbalanced:
        removed_count += 1

    return (result, removed_count)
