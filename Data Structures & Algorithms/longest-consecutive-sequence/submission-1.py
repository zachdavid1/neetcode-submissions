class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        if len(nums) == 0:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        max_seq = 0
        count = 0
        for element in nums:
            seen.add(element)
        for num in range(min_val, max_val +1):
            if num in seen:
                count+=1
                if count > max_seq:
                    max_seq = count
            else:
                count = 0
        return max_seq





        