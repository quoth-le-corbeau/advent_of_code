import time


INPUT_PATH = "my_inputs/{year}/day_{day}/{file}.txt"


def timer(func):
    def solution_function(*args, **kwargs):
        timer_start = time.perf_counter()
        func(*args, **kwargs)
        print(f"Elapsed {time.perf_counter() - timer_start:2.4f} seconds.")

    return solution_function
