class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        start = 0
        count = 0

        while start < n:
            prev = nums[start]
            curr_idx = start

            while True:
                # shift element by k places
                next_idx = (curr_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]

                curr_idx = next_idx
                count += 1

                if curr_idx == start:
                    break

            if count >= n:
                break

            start += 1
