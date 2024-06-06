#The problem is to search for a element in a 2D matrix and return bool if it exist.
#The constraint is to solve the problem in O(log m*n). So, we can approach using binary search.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # r and c denoted rows and cols in the matrix.
        r , c = len(matrix) , len(matrix[0])

      
        #are declared to find if the integer exist in a row or not.
        top , bot = 0, r - 1

        while top <= bot:
            row = (top + bot) // 2

            #since each row in the matrix follows a non-decreasing order we can compare if the target is larger than the last element of the list.
            if target > matrix[row][-1] :
                top = row + 1
            #or lesser than the first element of the 'row' the comparison is made.
            elif target < matrix[row][0] :
                bot = row - 1
            else :
                break

      
        #we can straight away return it if this condition fails meaning that the top or bottom row has gone out of bound while searching for the target which is out of range.
        if not (top <= bot):
            return False

        #row variable is the row where the element may exist.
        row = (top + bot) // 2

        #now performing the classic Binary search to find the target.
        l, r = 0, c - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            elif target == matrix[row][m]:
                return True
        return False

