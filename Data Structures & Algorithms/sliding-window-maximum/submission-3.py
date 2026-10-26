class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tuple_nums = [(num, index) for index, num in enumerate(nums)]
        tuple_nums.sort(reverse=True)

        # then just O(n) loop through this into (n - k + 1 buckets)

        buckets = [None for _ in range(len(nums) - k + 1)]
        empty = len(buckets)
        tuple_index = 0
        while empty > 0:
            # go from descending and paste the largest number with the above index -> bucket mapping
            # bucket n => index n to index n + k - 1
            # index n => buckets n - k + 1 to n (if valid)
            num, index = tuple_nums[tuple_index]
            # check validity
            start_bucket = max(0, index - k + 1)
            end_bucket = min(len(buckets) - 1, index)

            for i in range(start_bucket, end_bucket + 1):
                # Only fill the bucket if it's empty!
                if buckets[i] is None: 
                    buckets[i] = num
                    empty -= 1

            tuple_index += 1
        
        return buckets



            

