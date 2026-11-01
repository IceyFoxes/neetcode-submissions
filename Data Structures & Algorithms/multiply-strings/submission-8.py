class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                number1 = int(num1[i])
                number2 = int(num2[j])
                powers = len(num1) - i - 1 + len(num2) - j - 1
                res[powers] += number1 * number2
        
        for k in range(len(res) - 1):
            res[k + 1] += res[k] // 10
            res[k] %= 10
        
        result = [str(digit) for digit in reversed(res)]
        return ''.join(result).lstrip('0')
        