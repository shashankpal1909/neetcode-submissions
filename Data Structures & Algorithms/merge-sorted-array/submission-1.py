class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m - 1, n - 1
        idx = m + n - 1

        # merge from rear end to avoid overriding elements
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        # copy remaining elements from `nums2`
        while j > -1:
            nums1[idx] = nums2[j]
            idx, j = idx - 1, j - 1
