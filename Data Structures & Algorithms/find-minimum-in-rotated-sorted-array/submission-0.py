class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        min_val = float('inf')
        while l<=r:
            mid = (l+r) // 2

            if nums[r] >= nums[mid]:
                #rhs is sorted
                if nums[mid] < min_val:
                    min_val = nums[mid]
                r = mid -1
            else:
                #lhs is sorted
                if nums[l] < min_val:
                    min_val = nums[l]
                l = mid +1
            
        return min_val
                






        