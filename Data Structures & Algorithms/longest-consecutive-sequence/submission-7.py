class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if not nums:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        max_len = 0
        curr_len = 0
        
        for element in range(min_val, max_val +1):
            if element in seen:
                curr_len +=1
            else:
                curr_len = 0
            if curr_len > max_len:
                max_len = curr_len
        return max_len

        
