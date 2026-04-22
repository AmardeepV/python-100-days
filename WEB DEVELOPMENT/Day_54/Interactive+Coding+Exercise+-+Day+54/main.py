import time


def speed_calc_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        return f"{func.__name__} run speed {end_time - start_time}s"

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == "__main__":
    print(fast_function())
    print(slow_function())
