# To sort an array without any in-built functions and achieve a time complexity of O(n log n), with minimal space complexity.
# Solution : with merge sort the required conditions can be met.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums, 0, len(nums) - 1)

    # calling function mergesort with parametres nums, s(start index), e(end index).
    def mergesort(self, nums : List[int], s, e) -> List[int]:
        if e - s + 1 <= 1:
            return nums

        m = (e + s) // 2
      
        #the function is called recursively after splitting into two halves until there is only one element in the list.
        self.mergesort(nums, s, m)
        self.mergesort(nums, m + 1, e)
      
        #the divided elements are sorted and merged in merge function.
        self.merge(nums, s, m, e)

        return nums

    def merge(self, arr : List[int], s : int, m : int, e : int) -> None:
        left = arr[s : m + 1]
        right = arr[m + 1 : e + 1]

        # three pointers are used for comparison of elements in the left and right list.
        i , j, k = 0, 0, s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

        #if one list is sorted and merged while the other(left/right) still has some elements then those elements can be added directly to the list.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
