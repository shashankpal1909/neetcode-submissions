class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = defaultdict(int)

        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum == k:
                count += 1

            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1

        return count
