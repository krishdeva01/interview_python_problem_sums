prices = [7,1,3,4,5,4]
def stock_prices(prices):
  max_profit = 0
  cheap_price = float("inf")
  for price in prices:
    if price < cheap_price:
      cheap_price = price
    max_profit = max(max_profit, price-cheap_price)
  return max_profit
print(stock_prices(prices))


# ### **Output:**  
# `4` (The maximum profit is 4, achieved by buying at price 1 and selling at price 5).

# ### **Time and Space Complexity:**
# - **Time Complexity:** \( O(n) \) (only one loop over the array).
# - **Space Complexity:** \( O(1) \) (no extra space used apart from a few variables).