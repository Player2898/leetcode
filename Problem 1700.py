class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        count = Counter(students) #mapping the students as per their preferences.
        for s in sandwiches:
            if count[s] > 0: #checking if the students with a specific preference are there.
                result -= 1
                count[s] -=1
            else:
                return result
        return result
