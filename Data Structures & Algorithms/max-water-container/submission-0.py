class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        i, j = 0, n - 1
        max_area = 0

        while i < j:
            curr_area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, curr_area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
