class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        bucket = [[] for _ in range(len(nums) + 1)]

        counter = Counter(nums)
        
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res





