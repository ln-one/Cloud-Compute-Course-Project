import math
import sys
import time

from mpi4py import MPI


def f(x):
    return 4.0 / (1.0 + x * x)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
h = 1.0 / n

if rank == 0:
    chunk = n // size
    ranges = []
    for worker in range(size):
        start_i = worker * chunk
        end_i = n if worker == size - 1 else start_i + chunk
        ranges.append((start_i, end_i))
else:
    ranges = None

# Scatter: rank 0 sends one integration interval range to each MPI process.
start_i, end_i = comm.scatter(ranges, root=0)

start = time.perf_counter()
local_sum = 0.0
for i in range(start_i, end_i):
    x = (i + 0.5) * h
    local_sum += f(x)

# Reduce: every process sends local_sum to rank 0, rank 0 sums all partial areas.
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    pi = total_sum * h
    elapsed = time.perf_counter() - start
    print(f"mpi_blocking p={size} n={n} pi={pi:.10f} time={elapsed:.6f}s error={abs(math.pi - pi):.6e}")
