#you are given a list, where from a certain integer all the versions are bad.
#you need to find the first bad version.
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # setting low and high as 1 and n.
        l , h = 1, n

        #the loop would run until first bad version is found (i.e.) l=m=h.
        while l <= h:
            m = (l + h) // 2
            # if a version is found bad, also check the previous version. Since we need the first bad version.
            if isBadVersion(m):
                h = m - 1
            elif not isBadVersion(m):
                l = m + 1
        return l
