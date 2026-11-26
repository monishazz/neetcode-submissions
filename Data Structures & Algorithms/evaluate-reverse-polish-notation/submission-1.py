class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif s == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif s == '-':
                a , b = int(stack.pop()) , int(stack.pop())
                stack.append(b - a)
            elif s == '/':
                a , b = int(stack.pop()) , int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(s))
        return stack[0]      