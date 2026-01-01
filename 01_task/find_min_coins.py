def find_min_coins(sum: int, denomination: list[int]) -> dict[int, int]:
    K = [float('inf')] * (sum + 1)
    K[0] = 0
    used_coins = [0] * (sum + 1)

    for i in range(sum+1):
        for coin in denomination:
            if coin > i:  # try next coin
                continue

            if K[i-coin] + 1 < K[i]:
                K[i] = K[i-coin] + 1
                used_coins[i] = coin

    if K[sum] == float('inf'):  # unable to provide sum
        return {}

    res = {}
    # go backward in used coins to restore the denomination of the coins
    while (sum):
        used_coin = used_coins[sum]
        res[used_coin] = res.get(used_coin, 0) + 1
        sum -= used_coin

    return res
