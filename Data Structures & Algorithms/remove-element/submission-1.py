class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        count = 0

        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                count += 1
            else:
                i = i + 1

        return len(nums) - count
