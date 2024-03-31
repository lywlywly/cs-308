import json
import time


def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise Exception("n should be larger than or equal to 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = 0

    for i in range(3, n + 1):
        fib = fib_minus_2 + fib_minus_1
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib

    return fib


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise Exception("n should be larger than or equal to 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    n_i = 1000
    n_r = 41
    runtimes_iterative: list[float] = []
    runtimes_recursive: list[float] = []

    for i in range(1, n_i + 1):
        start_time = time.time()
        fib_iterative = fibonacci_iterative(i)
        end_time = time.time()
        iterative_runtime = end_time - start_time
        runtimes_iterative.append(iterative_runtime)

    for i in range(1, n_r + 1):
        start_time = time.time()
        fib_recursive = fibonacci_recursive(i)
        end_time = time.time()
        recursive_runtime = end_time - start_time
        runtimes_recursive.append(recursive_runtime)

    with open("runtimes_iterative.json", "w") as f:
        json.dump(runtimes_iterative, f)
    with open("recursive_runtime.json", "w") as f:
        json.dump(runtimes_recursive, f)


main() if __name__ == "__main__" else None
