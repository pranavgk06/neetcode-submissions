class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        max_future = 0
        for i in range(len(prices)-1,-1,-1):         
            price = prices[i]
            max_profit = max(max_profit, max_future - price)
            max_future = max(max_future, price)
        return max_profit

            
        