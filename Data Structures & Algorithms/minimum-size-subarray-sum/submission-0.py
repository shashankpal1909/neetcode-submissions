class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        subarray_sum = 0
        res = len(nums) + 1

        for r in range(len(nums)):
            # increase sliding window
            subarray_sum += nums[r]
            
            # shrink window until valid
            while subarray_sum >= target:
                res = min(res, r - l + 1)
                subarray_sum -= nums[l]
                l += 1

        return 0 if res > len(nums) else res
