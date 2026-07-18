class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        c1, c2 = None, None
        v1, v2 = 0, 0

        threshold = len(nums) // 3

        for num in nums:
            if c1 is None:
                c1 = num
                v1 = 1

            elif c2 is None and num != c1:
                c2 = num
                v2 = 1

            elif c1 == num:
                v1 += 1

            elif c2 == num:
                v2 += 1

            else:
                v1 -= 1
                v2 -= 1

            if v1 == 0:
                c1 = None
            if v2 == 0:
                c2 = None
            

        v1, v2 = 0, 0
        for num in nums:
            if num == c1:
                v1 += 1
            if num == c2:
                v2 += 1

        result = []

        if v1 > threshold:
            result.append(c1)
        if v2 > threshold:
            result.append(c2)

        return result
