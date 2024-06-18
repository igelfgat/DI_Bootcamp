from utils.math_utils import add_two


# __name__ = "__main__" - when file is running directly
# __name__ = SOMETHING ELSE - when file is not running directly

if __name__ == "__main__":
    result = add_two(5, 10)
    print(result)
