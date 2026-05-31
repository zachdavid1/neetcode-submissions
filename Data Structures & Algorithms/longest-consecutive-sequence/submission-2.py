class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 0
        seen = set(nums)
        for num in nums:
            count = 0
            while (num + count) in seen:
                count +=1
                if count > max_count:
                    max_count = count
        return max_count
        
        
        