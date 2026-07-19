class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i, j = 0, 1

        while i < j and j < n:
            while abs(j - i) <= k and j < n:
                if nums[i] == nums[j]:
                    return True
                j += 1
            i, j = i + 1, i + 2

        return False
