class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            
            # two sum on a sorted list
            while j < k:
                current = nums[i] + nums[j] + nums[k]

                if current > 0:
                    k -= 1
                elif current < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip same consecutive elements
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return result
