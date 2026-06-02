class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        if not nums:
            return 0
        
        for num in seen:
            if num-1 not in seen:
                curr_len = 1
                curr = num
                while curr +1 in seen:
                    curr = curr+1
                    curr_len +=1
                if curr_len > max_len:
                    max_len = curr_len
        return max_len


        
