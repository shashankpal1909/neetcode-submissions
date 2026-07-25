class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = [(num, abs(num - x)) for num in arr]
        res.sort(key=lambda item: (item[1], item[0]))
        return sorted([item[0] for item in res[:k]])
