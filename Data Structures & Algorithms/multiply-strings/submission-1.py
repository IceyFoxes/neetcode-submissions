class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                number1 = int(num1[i]) * pow(10, len(num1) - i - 1)
                number2 = int(num2[j]) * pow(10, len(num2) - j - 1)
                res += number1 * number2

        return str(res)
        