import json
from option_a.solution import separate_paren_groups
from option_b.solution import starts_one_ends


def run_option_a():
    with open("option_a/tests.json") as f:
        tests = json.load(f)["test_case"]

    passed = 0

    for t in tests:
        inp, expected = t["input"], t["expected"]
        result = separate_paren_groups(inp[0], inp[1])

        print("A Input:", inp)
        print("Expected:", expected)
        print("Got:", result)
        print("-")

        if result == tuple(expected):
            passed += 1

    print("Option A:", passed, "/", len(tests))


def run_option_b():
    with open("option_b/tests.json") as f:
        tests = json.load(f)["test_case"]

    passed = 0

    for t in tests:
        inp, expected = t["input"], t["expected"]
        result = starts_one_ends(*inp)

        print("B Input:", inp)
        print("Expected:", expected)
        print("Got:", result)
        print("-")

        if result == expected:
            passed += 1

    print("Option B:", passed, "/", len(tests))


if __name__ == "__main__":
    run_option_a()
    run_option_b()
