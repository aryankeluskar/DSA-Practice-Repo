class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for i in tokens:
            if i in ops:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    stack.append(num1 + num2)
                if i == '*':
                    stack.append(num1 * num2)
                if i == '/':
                    stack.append(num1 / num2)
                if i == '-':
                    stack.append(num1 - num2)

            else:
                stack.append(int(i))

        return int(stack.pop())