class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        l, r = 0, 1

        maxProfit = 0
        # while r < len(prices):
        #     # compute current profit and update max value
        #     profit = prices[r] - prices[l]
        #     maxProfit = max(maxProfit, profit)

        #     # conditionally expand the window
        #     if r < len(prices) - 1:
        #         if prices[r + 1] > prices[r]:
        #             r += 1
        #         else:
        #             l += 1
        #     else:
        #         l += 1

        #     # if the two numbers now overlap expand the window
        #     if l == r:
        #         r += 1

        # return maxProfit
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            if prices[r] < prices[l]:
                l = r
            
            r += 1

        return maxProfit