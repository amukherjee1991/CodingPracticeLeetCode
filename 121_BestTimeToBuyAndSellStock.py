class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return None
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit =max(max_profit, prices[i]-min_price)
        return max_profit