class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._merge_sort(nums)

    def _merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        arr1 = self._merge_sort(arr[:mid])
        arr2 = self._merge_sort(arr[mid:])

        return self._merge(arr1, arr2)

    def _merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        res = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1

        while j < len(arr2):
            res.append(arr2[j])
            j += 1

        return res
