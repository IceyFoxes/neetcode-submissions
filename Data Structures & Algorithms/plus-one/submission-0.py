class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        reverse = digits[::-1]
        i = 0

        while carry > 0 and i < len(digits):
            reverse[i] += 1
            carry = max(0, reverse[i] - 9)
            reverse[i] %= 10
            i += 1
        
        if carry > 0:
            reverse.append(carry)
        
        return reverse[::-1]
        