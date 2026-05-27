class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_max = 0

        for i in range(len(prices)-1, -1, -1):
            curr_max = max(curr_max, prices[i])
            max_profit = max(max_profit, curr_max - prices[i])
        return max_profit 
        