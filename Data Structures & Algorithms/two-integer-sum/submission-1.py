class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, num in enumerate(nums):
            nums_map[num] = idx

        for idx, num in enumerate(nums):
            if (target - num) in nums_map and nums_map[target - num] != idx:
                return sorted([idx, nums_map[target - num]])

        return []
