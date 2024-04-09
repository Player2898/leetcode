class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation.isdigit() or operation[0] == '-':
                stack.append(int(operation))
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                d = stack.pop() 
                stack.append(d)
                stack.append(d*2)
            elif operation == "+":
                top = stack.pop()
                second_top = stack.pop()
                result = top + second_top
                stack.append(second_top)
                stack.append(top)
                stack.append(result)
        #print(stack)
        return sum(stack)
