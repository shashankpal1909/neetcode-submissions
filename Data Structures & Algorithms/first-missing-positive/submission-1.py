class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            num = nums[i]
            if i + 1 != num:
                if 0 <= num - 1 < len(nums) and nums[i] != nums[num - 1]:
                    nums[i], nums[num - 1] = nums[num - 1], nums[i]
                    i -= 1
            i += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1

        return len(nums) + 1
