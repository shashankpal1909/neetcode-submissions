class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq_0, freq_1, freq_2 = 0, 0, 0

        for num in nums:
            if num == 0:
                freq_0 += 1
            elif num == 1:
                freq_1 += 1
            else:
                freq_2 += 1

        idx = 0

        while freq_0 > 0:
            nums[idx] = 0
            idx += 1
            freq_0 -= 1

        while freq_1 > 0:
            nums[idx] = 1
            idx += 1
            freq_1 -= 1
            
        while freq_2 > 0:
            nums[idx] = 2
            idx += 1
            freq_2 -= 1
