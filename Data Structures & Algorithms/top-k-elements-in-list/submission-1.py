class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums)
        freq_arr = [[] for _ in range(0, len(nums) + 1)]

        for val, freq in freq_map.items():
            freq_arr[freq].append(val)

        result = []
        for arr in freq_arr[-1::-1]:
            if len(result) == k:
                break
            for val in arr:
                if len(result) < k:
                    result.append(val)
                else:
                    break

        return result
