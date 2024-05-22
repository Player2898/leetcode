class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_elem = Counter(nums) #to count no.of occurence of each element in nums.
        key_val = dict(count_elem)
        for key,val in key_val.items():
            if key_val[key] > 1:
                return True
        return False 
