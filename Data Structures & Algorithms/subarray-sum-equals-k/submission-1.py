class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = [0] * len(nums)
        prefix_map = defaultdict(int)

        count = 0

        for idx, num in enumerate(nums):
            prefix_sum[idx] = num if idx == 0 else num + prefix_sum[idx - 1]

            if prefix_sum[idx] == k:
                count += 1

            count += prefix_map[prefix_sum[idx] - k]
            prefix_map[prefix_sum[idx]] += 1

        return count
