class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    if nums[j] == nums[i]:
                        return True
        return False