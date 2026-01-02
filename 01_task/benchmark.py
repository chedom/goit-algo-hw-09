import timeit

from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

def benchmark_algo(find_func, sum, denomination, number):
    timer = timeit.Timer(lambda: find_func(sum, denomination))
    return timer.timeit(number=number)


def run_benchmark_for_sum(sum, denomination):
    algos = [
        ("greedy", find_coins_greedy),
        ("dynamic programming", find_min_coins),
    ]

    for algo in algos:
        algo_name, algo_func = algo
        res = benchmark_algo(algo_func, sum, denomination, 100)
        print(f"Run bench for {algo_name.capitalize()} for sum: {sum}: {res}")


def run_benchmark():
    denomination = [50, 25, 10, 5, 2, 1]
    sums = [19, 113, 589, 1873, 12891]
    print("Start benchmark")

    for sum in sums:
        run_benchmark_for_sum(sum, denomination)
    print("End benchmark")
