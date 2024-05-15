class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low + high)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
#This valid perfect square problem is solved using binary search as it can be solved in O(log n) computational time.
