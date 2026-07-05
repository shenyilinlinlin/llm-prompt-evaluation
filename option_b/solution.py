def starts_one_ends(n, x, y):
    if n < 1 or n > 5 or x < 0 or x > 9 or y < 0 or y > 9:
        return -1

    def count_start():
        if n == 1:
            return 1
        if x == 0:
            return 0
        return 10 ** (n - 1)

    def count_end():
        return 10 ** (n - 1)

    start = count_start()
    end = count_end()

    if n == 1:
        both = 1 if x == y else 0
    elif n == 2:
        both = 1
    else:
        both = 10 ** (n - 2)

    result = start + end - both

    return result if result > 0 else -1
