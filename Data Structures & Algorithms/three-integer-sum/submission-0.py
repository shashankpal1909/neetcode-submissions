class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums_hash = Counter(nums)

        result = set()
        for i in range(n):
            for j in range(i + 1, n):
                a, b, c = nums[i], nums[j], -(nums[i] + nums[j])

                nums_hash[a] -= 1
                nums_hash[b] -= 1

                if c in nums_hash and nums_hash[c] > 0:
                    result.add(tuple(sorted([a, b, c])))

                nums_hash[a] += 1
                nums_hash[b] += 1

        return list(result)
