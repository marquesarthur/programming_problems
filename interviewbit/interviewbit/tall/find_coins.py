def f_equal(a, b):
   return abs(a - b) < 0.000001


def find_min_coins(target, results, new_result, coins, idx):
    if idx == -1:
        return

    current_change = coins[idx]
    if target - current_change > 0.0:
        new_result[idx] += 1

        new_new = new_result
        find_min_coins(target - current_change, results, new_new, coins, idx)
    elif f_equal(target, current_change):
        new_result[idx] += 1
        results.append(new_result)
        return
    else:
        new_idx = idx - 1
        find_min_coins(target, results, new_result, coins, new_idx)






def getChange(bill, price):
    coins = [.01, .05, .10 , .25, 0.5, 1 ] # 1c, 5c, 10c, 25c, 50c, and $1

    result = []
    target =  bill - price
    new_result = [0, 0, 0, 0, 0, 0]
    find_min_coins(target, result, new_result, coins, len(coins) - 1)

    idx_best = -1
    min_sum = 999999
    for i, r in enumerate(result):
        if sum(r) < min_sum:
            idx_best = i
    if not result:
        return new_result
    return result[idx_best]



def main():
    print(getChange(5, 0.99)) # [1,0,0,0,0,4]
    print(getChange(3.14, 1.99)) #     return [0, 1, 1, 0, 0, 1]
    print(getChange(4, 3.14)) #     return [1, 0, 1, 1, 1, 0]
    print(getChange(0.45, 0.34)) #     return [1, 0, 1, 0, 0, 0]




if __name__ == "__main__":
    main()

