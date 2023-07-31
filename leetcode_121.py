def StockProfit(prices):
    #setting 1st as minimum price
    min_price=prices[0]
    profit=0

    for i in range(1,len(prices)):
        #resetting minimum price if stock has gone lower
        min_price=min(min_price,prices[i])

        #calculating recent profit
        current_profit= prices[i] - min_price

        #optimizing max profit
        profit=max(profit,current_profit)
    
    return profit

print(StockProfit([7,1,3,6,4]))