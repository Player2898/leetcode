class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 #counts the element that are not val  and if the if condition is not passed it will not be incremented so that we can keep track of val's position
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] 
                count += 1
        return count
