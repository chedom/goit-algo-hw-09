def find_coins_greedy(sum: int, denomination: list[int]) -> dict[int, int]:
    denomination = sorted(denomination, reverse=True)
    res = {}

    for coin in denomination:
        num = sum // coin

        if not num:
            continue  # try smaller coin

        res[coin] = num
        sum %= coin

        if not sum:  # early return if all coins are found
            return res

    return res
