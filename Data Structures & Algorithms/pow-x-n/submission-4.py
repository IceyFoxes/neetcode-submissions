class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        base = x
        exponent = n

        while exponent != 0:
            if exponent % 2 != 0:
                result *= base
                exponent = exponent - 1 if exponent > 0 else exponent + 1
            else:
                base *= base
                exponent //= 2
        
        return result if n > 0 else 1 / result