def find_coins_greedy(sum: int, denomination: list[int]) -> dict[int, int]:
    denomination.sort(reverse=True)
    res = {}

    coin_idx = 0
    # proceed until the last coin is not bigger than sum 
    # not possible if we have a coin with `1` denomination
    while (sum >= denomination[-1]):
        coin_val = denomination[coin_idx]

        if coin_val > sum:  # move to the smaller coin
            coin_idx += 1
            continue

        sum -= coin_val
        print(coin_val)
        res[coin_val] = res.get(coin_val, 0) + 1

    return res
