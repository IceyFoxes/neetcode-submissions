class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = Counter(nums)
        dominant = max(counts, key=counts.get)
        total = counts[dominant]
        left_count = 0

        for i in range(len(nums) - 1):
            left_count += nums[i] == dominant
            right_count = total - left_count

            if (left_count * 2 > i + 1 and
                right_count * 2 > len(nums) - i - 1):
                return i

        return -1