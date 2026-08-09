class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit=0
        MinPrice=float('inf')
        for price in prices:
            if price <MinPrice:
                MinPrice=price
            elif price-MinPrice>MaxProfit:
                MaxProfit=price-MinPrice
        return MaxProfit
            