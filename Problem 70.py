#climbing stairs- Given 'n' stairs generate in how many distinct way n stairs can be climbed using just 1 and 2 as the number of stairs you can climb at a time.
#solution : this problem can be solved using fibonacci approach. Hence,n1 and n2 are assigned the values 1.
class Solution:
    def climbStairs(self, n: int) -> int:
        n1 , n2 = 1 , 1     

        for i in range(n - 1):
            temp = n1
            n1 = n1 + n2
            n2 = temp
        return n1
