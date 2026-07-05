from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool = False) -> Tuple[List[str], int]:
    groups = []
    current = []
    depth = 0
    removed = 0

    for ch in paren_string:
        if ch not in "()":
            continue

        if ch == '(':
            if depth == 0:
                current = []
            depth += 1
            current.append(ch)

        else:  # ')'
            if depth > 0:
                depth -= 1
                current.append(ch)

                if depth == 0:
                    groups.append("".join(current))
                    current = []
            else:
                if remove_unbalanced:
                    removed += 1

    if remove_unbalanced:
        removed += depth

    return groups, removed
