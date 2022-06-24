# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# def maxProfit(stockPrices):
#   l = 0
#   r = 1
#   maxProfit = 0
#   for r in range(1,len(stockPrices)):
#     profit = stockPrices[r] - stockPrices[l]
#     if profit > 0:
#       if profit > maxProfit:
#         maxProfit = profit
#         r += 1
#       else:
#         r += 1
#     else:
#       l += 1
#       r += 1
#   return maxProfit

# We have r += 1 in all conditions, so we can just move it outside the if else conditions and do it in every loop
# if profit > maxProfit:
#         maxProfit = profit
# Can be written as maxProfit = max(maxProfit, profit)
def maxProfit(stockPrices):
  l = 0
  r = 1
  maxProfit = 0
  for r in range(1,len(stockPrices)):
    profit = stockPrices[r] - stockPrices[l]
    if profit > 0:
      maxProfit = max(maxProfit, profit)
    else:
      l += 1
    r += 1
  return maxProfit

print('Final max profit ' + str(maxProfit([4,9,3,5,17,9,7,23,20])))


# If need to return the days of buying of selling insdead of mas profit

def maxProfitUpdate(stockPrices):
  l = 0
  r = 1
  maxProfit = 0
  for r in range(1,len(stockPrices)):
    profit = stockPrices[r] - stockPrices[l]
    if profit > 0:
      if profit > maxProfit:
        maxProfit = profit
        bestBuyingDay = l + 1
        bestSellingDay = r + 1
    else:
      l += 1
    r += 1
  return [bestBuyingDay,bestSellingDay]

print('Best buying and selling days are ' + str(maxProfitUpdate([4,9,3,5,17,9,7,23,20])))