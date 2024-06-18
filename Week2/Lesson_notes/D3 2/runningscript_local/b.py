from a import add_two


def add_and_multiply(n1, n2) -> int:
    addition_result = add_two(n1, n2)
    return n1 * addition_result + n2 * addition_result
