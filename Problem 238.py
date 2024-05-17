class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dummy = nums[::-1]
        prefix = [] 
        suffix = []
        mul1 = 1
        mul2 = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(mul1) #initially for first element prefix is 1 since there are no other elements before index 0.
                suffix.append(mul2) #initially for last element suffix is 1 since there are no other elements after index n.
            else:
                mul1 *= nums[i-1] #hold the product of all integers before the index i except index 0.
                mul2 *= dummy[i-1] #hold the product of all integers after the index i except index 0(note that dummy is reversed list to handle suffix).
                prefix.append(mul1) 
                suffix.append(mul2)
        return [a * b for a,b in zip(prefix,suffix[::-1])] #product of prefix and suffix gives you the product of an array except self.
        
