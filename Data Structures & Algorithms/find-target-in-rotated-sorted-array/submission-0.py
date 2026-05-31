class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        
        
        while l<=r:
            mid = (r + l) //2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                #lhs sorted
                if target < nums[mid] and target >= nums[l]:
                    r = mid -1
                else:
                    l = mid +1
            else:
                #rhs is sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return -1
        

            


            

        