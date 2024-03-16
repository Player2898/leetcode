class Solution:
    def reverse(self, x: int) -> int:
        #flag handles the negative integer.
        flag = -1 if x < 0 else 1
        x *= flag
        reverse = 0
        while x != 0:
            reverse = reverse * 10 + (x % 10)
            #splits the rest of the integer except the last digit and the iteration is repeated until it becomes 0.
            x = x//10
        return 0 if (reverse * flag > (2**31 - 1) or
        reverse * flag < (-2**31)) else reverse * flag
        
