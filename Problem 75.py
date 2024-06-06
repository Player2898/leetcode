class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #approaching to solve this sorting problem using bucket sort.
        #"count" variable acts as the bucket that stores the repeatation of the numbers in the "nums" list with the size range of numbers used in the list.
        #initial all the numbers as 0 in the counts list.

        counts = [0,0,0]
        
        #each time the loop iterates through the list when it comes accross the same integer it will increase its count.
        for n in nums:
            counts[n] += 1

        #variable 'i' acts as the pointer to do the inplace operation in the nums list.
        i = 0

        #outer-loop iterates through the length of count.
        #inner-loop iterates through the integer item in the list. ex: if the item in the list is 2 two changes are made in the nums list with corresponding n.
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1


        
