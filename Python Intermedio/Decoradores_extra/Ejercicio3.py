from datetime import datetime


def validate_numbers(func):
    def wrapper(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be numeric")

        return func(*args, **kwargs)

    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        current_date = datetime.now()

        print(
            f"func: {func.__name__} - "
            f"args: {', '.join(map(str, args))} - "
            f"[{current_date}] - "
            f"Result: {result}"
        )

        return result

    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


result = multiply(3, 4)

print(f"Result {result}")