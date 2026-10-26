class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        pair_sum = defaultdict(list)
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                pair_sum[nums[i] + nums[j]].append((i, j))

        for k in range(n):
            target = -nums[k]
            for i, j in pair_sum.get(target, []):
                if k != i and k != j:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)

        return [list(triplet) for triplet in res]

        


        
