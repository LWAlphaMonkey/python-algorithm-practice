"""
Function to find out maximum profit by buying
& selling a share within a day
"""

from __future__ import print_function

def max_stock_profit(prices):
    """
    Take in array of prices as parameter
    Return the max possible profit of the day

    P.S. If no profit is possible, return -1
         A max profit of 0 is treated as any other max profit value
    """
    max_profit = -1
    change_buy_price = True

    for idx, price in enumerate(prices):
        if idx == len(prices) -1:
            break

        if change_buy_price:
            buy_price = price

        if idx + 1 < len(prices):
            sell_price = prices[idx + 1]

        if sell_price < buy_price:
            change_buy_price = True
        else:
            temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit
            change_buy_price = False

    return max_profit

print(max_stock_profit([32, 46, 55, 38, 40, 48, 42, 5, 30]))
print(max_stock_profit([10, 18, 4, 5, 9, 6, 16, 12]))
print(max_stock_profit([10, 8, 7, 6]))
print(max_stock_profit([10, 8]))
