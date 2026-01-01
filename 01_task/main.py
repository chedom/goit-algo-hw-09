from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def main():
    denomination = [50, 25, 10, 5, 2, 1]
    res1 = find_coins_greedy(113, denomination)
    print("res1", res1)
    res2 = find_min_coins(113, denomination)
    print("res2", res2)


if __name__ == '__main__':
    main()
