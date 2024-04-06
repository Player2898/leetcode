class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")": 
                if len(stack) == 0: #if there are no opening brackets in stack
                    s = s[:i] + "!" + s[i + 1:] #replacing the left out bracket with a special character
                else:
                    stack.pop()
        if stack: #if there are any left out opening brackets
            for j in stack:
                s = s[:j] + "!" + s[j + 1:]
                
            
        if "!" in s:
            s = s.replace("!", '')
        return s
