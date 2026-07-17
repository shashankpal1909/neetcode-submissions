class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            prefix[i] = (prefix[i - 1] if i > 0 else 1) * nums[i]

        for i in range(n - 1, 0, -1):
            suffix[i] = (suffix[i + 1] if i < n - 1 else 1) * nums[i]

        return [
            (1 if i == 0 else prefix[i - 1]) * (1 if i == n - 1 else suffix[i + 1])
            for i in range(n)
        ]
