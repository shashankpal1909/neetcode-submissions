class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i, j = 0, 0

        nums_set = set()

        for j in range(n):
            if j - i > k:
                # shift window
                nums_set.remove(nums[i])
                i += 1

            if nums[j] in nums_set:
                return True

            nums_set.add(nums[j])

        return False
