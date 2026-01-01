from find_coins_greedy import find_coins_greedy


def main():
    denomination = [50, 25, 10, 5, 2, 1]
    res = find_coins_greedy(113, denomination)
    print(">>>", res)


if __name__ == '__main__':
    main()
