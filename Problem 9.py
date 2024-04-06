class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : #if it is a non positive integer
            return False
        rev = 0
        og = x
        while x > 0:
            dig =  x % 10 #seperating the units digit from the OG integer
            rev = rev * 10 + dig #reversing takes place during each iteration
            x = x // 10
        return rev == og
