class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            prefix[i] = (prefix[i - 1] if i > 0 else 1) * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            suffix[i] = (suffix[i + 1] if i < len(nums) - 1 else 1) * nums[i]

        return [
            (1 if i == 0 else prefix[i - 1]) * (1 if i == len(nums) - 1 else suffix[i + 1])
            for i in range(len(nums))
        ]
