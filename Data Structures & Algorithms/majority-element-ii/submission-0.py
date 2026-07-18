class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        majority_threshold = len(nums) // 3

        result = []
        for key, val in freq_map.items():
            if val > majority_threshold:
                result.append(key)

        return result
