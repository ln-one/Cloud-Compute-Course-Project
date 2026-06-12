import math
import sys
import time


def f(x):
    return 4.0 / (1.0 + x * x)


def integrate(n):
    h = 1.0 / n
    total = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        total += f(x)
    return total * h


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    start = time.perf_counter()
    pi = integrate(n)
    elapsed = time.perf_counter() - start
    print(f"serial n={n} pi={pi:.10f} time={elapsed:.6f}s error={abs(math.pi - pi):.6e}")

