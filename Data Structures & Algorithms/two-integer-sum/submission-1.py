class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, element in enumerate(nums):
            needed = target - element
            if needed in seen:
                return ([seen[needed], index])
            seen[element] = index
        return False


