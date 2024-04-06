class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ["()", "[]", "{}"]
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch =="{":
                stack.append(ch)
            elif ch == "}" or ch == ")" or ch == "]":
                if not stack: #when a closing bracket is reached when there are no opening ones
                    return False
                else:
                    empty = stack.pop() + ch #matching the bracket with the top of stack and current char
                    if empty not in brackets: #if the var empty is not matched with any in list
                        return False
        if stack: #when the stack is not empty
            return False
        else:
            return True
