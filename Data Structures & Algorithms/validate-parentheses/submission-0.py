class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if len(stack) == 0:
                current_top = None
            else:
                current_top = stack[-1]
            if (current_top == '{' and bracket =='}') or (current_top == '[' and bracket == ']') or (current_top == '(' and bracket == ')'):
                stack.pop()
            else:
                stack.append(bracket)
        if len(stack) ==0:
            return True
        return False
                
            
        