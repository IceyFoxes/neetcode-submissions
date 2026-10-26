class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i in range(len(nums)):
            num = nums[i]
            # better replacement
            while queue and num > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)

            if queue[0] < i - k + 1:
                # expired from window
                queue.popleft()
            
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res

        


        