class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        base = 1 / x if n < 0 else x
        exponent = abs(n)

        while exponent != 0:
            if exponent % 2 != 0:
                result *= base
                exponent = exponent - 1
            else:
                base *= base
                exponent //= 2
        
        return result