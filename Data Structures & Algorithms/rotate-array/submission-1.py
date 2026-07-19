class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums_map = defaultdict(int)
        for idx, num in enumerate(nums):
            nums_map[idx] = num

        for i in range(n):
            i_rot = (i + k) % n
            nums[i_rot] = nums_map[i]
