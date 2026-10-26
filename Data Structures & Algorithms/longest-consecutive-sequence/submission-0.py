class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        memo = defaultdict(int)
        
        def getLength(number):
            if number not in memo:
                if number - 1 in hashset:
                    memo[number] = getLength(number - 1) + 1
                else:
                    memo[number] = 1
            
            return memo[number]
        
        res = 0
        for number in nums:
            res = max(getLength(number), res)
        return res





        
