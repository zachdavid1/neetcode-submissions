class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_v = 0
        max_p = 0
        min_v = 10000
        for element in prices:
            if element < min_v:
                min_v = element
                max_v = element
            elif element > max_v:
                max_v = element
                profit = max_v - min_v
                if profit > max_p:
                    max_p = profit
        return max_p
            
        

            
            


        