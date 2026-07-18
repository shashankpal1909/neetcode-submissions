class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []
        
        for i in range(n):
            # skip over duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                # skip over duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1

                while k < l:
                    curr = nums[i] + nums[j] + nums[k] + nums[l]

                    if curr < target:
                        k += 1
                    elif curr > target:
                        l -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # skip over duplicates
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        
                        # skip over duplicates
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return result
