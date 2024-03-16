class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        output = ""
        
        for row in range(numRows):
            jump = (numRows - 1) * 2 
            for i in range(row, len(s),jump):
                output += s[i]

                #condition to handle the rows where there are zig elements that needs to be added in the string
                if (row>0 and row < numRows -1 and jump -(2*row) + i < len(s)):
                    output += s[jump - (2*row) + i]
        
        return output
