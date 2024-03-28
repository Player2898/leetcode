class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0  #i indicates first item of the list
        j = len(height) - 1 #j indicates last item of the list
        max_area = 0
        while i!= j:
            #depending on the smallest element of the list i or j pointer is increased or decreased.
            if height[i] <= height[j]:  
                cur_area = height[i] * (j - i)
                i += 1
            else:
                cur_area = height[j] * (j - i)
                j -= 1
            if cur_area > max_area:
                max_area = cur_area
        return max_area
             
