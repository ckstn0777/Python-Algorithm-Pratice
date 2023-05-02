
def solution(cost):
    max_total_profit = 0
    min_price = float("inf")
    first_buy_sell_profits = []

    # 앞으로 읽는 부분
    for i in range(len(cost)):
        min_price = min(min_price, cost[i])
        max_total_profit = max(max_total_profit, cost[i] - min_price)
        first_buy_sell_profits.append(max_total_profit)

    # 뒤로 읽는 부분
    max_price = -float("inf")
    for i in range(len(cost) - 1, 0, -1):
        max_price = max(max_price, cost[i])
        max_total_profit = max(max_total_profit, 
                               max_price - cost[i] + first_buy_sell_profits[i - 1])

    return max_total_profit


if __name__ == "__main__":
    cost = [12, 11, 13, 9, 12, 8, 14, 13, 15]

    print(solution(cost)) # 10이 정답임(9 -> 12, 8 -> 15)


