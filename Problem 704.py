#the problem is to search a target element through a sorted list and return its index.
#integers in the array are unique.
#approach using binary search algorithm to achieve the contraint of O(log n).

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
