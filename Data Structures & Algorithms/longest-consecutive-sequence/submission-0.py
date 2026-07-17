class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        freq_map = Counter(nums)
        max_count = 0

        for num in nums:
            count = 1

            seed = num + 1
            while freq_map.get(seed):
                count += 1
                seed += 1

            max_count = max(max_count, count)

        return max_count
