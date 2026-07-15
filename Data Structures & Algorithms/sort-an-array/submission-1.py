class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def _merge_sort(arr: List[int], l: int, r: int):
            if l >= r:
                return

            m = (l + r) // 2

            _merge_sort(arr, l, m)
            _merge_sort(arr, m + 1, r)
            _merge(arr, l, m, r)

        def _merge(arr: List[int], l: int, m: int, r: int) -> None:
            i, j, k = 0, 0, l

            arr1, arr2 = arr[l : m + 1], arr[m + 1 : r + 1]

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                k += 1

            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1

            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1

        _merge_sort(nums, 0, len(nums) - 1)
        return nums
