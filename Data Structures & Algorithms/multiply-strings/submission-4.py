class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                number1 = int(num1[i])
                number2 = int(num2[j])
                powers = len(num1) - i - 1 + len(num2) - j - 1
                mult = number1 * number2

                while mult > 0:
                    total = res[powers] + mult
                    res[powers] = total % 10
                    mult = total // 10
                    powers += 1
        
        result = [str(digit) for digit in reversed(res)]
        return ''.join(result).lstrip('0') or '0'
        