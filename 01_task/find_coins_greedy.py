def find_coins_greedy(sum: int, denomination: list[int]) -> dict[int, int]:
    denomination = sorted(denomination, reverse=True)
    res = {}

    for coin in denomination:
        num = 0
        while (coin <= sum):
            num += 1
            sum -= coin

        if num:  # do not track skipped coins
            res[coin] = num

        if not sum:  # early return if all coins are found
            return res

    return res
