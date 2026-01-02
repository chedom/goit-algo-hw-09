from benchmark import run_benchmark
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def not_optimal_case():
    sum = 6
    denomination = [4, 3, 1]

    print(find_coins_greedy(sum, denomination))  # {4: 1, 1: 2}
    print(find_min_coins(sum, denomination))  # {3: 2}


def main():
    # run benchmark
    run_benchmark()
    # test the case when greedy algo provide not optimal result
    not_optimal_case()


if __name__ == '__main__':
    main()
