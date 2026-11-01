class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumSquareDigits(number):
            result = 0
            while number > 0:
                remainder = number % 10
                number = number // 10
                result += remainder * remainder
            return result

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumSquareDigits(n)

        return True