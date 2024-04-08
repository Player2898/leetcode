class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1 #counts the unique values
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i] #left pointer holds the incremented position if the values are not different
                left += 1
        return left
