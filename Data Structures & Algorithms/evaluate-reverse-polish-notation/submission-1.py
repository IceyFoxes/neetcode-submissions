class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')

        def operate(num1, num2, operator):
            if token == "+":
                return num1 + num2
            if token == "-":
                return num1 - num2
            if token == "*":
                return num1 * num2
            if token == "/":
                return num1 / num2

        for token in tokens:
            if token in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                result = operate(num1, num2, token)
                stack.append(result)
            else:
                stack.append(token)

        return int(stack[0])
