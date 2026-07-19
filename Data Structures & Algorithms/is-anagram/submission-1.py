class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_arr = [0] * 26

        for char in s:
            freq_arr[ord(char) - ord("a")] += 1

        for char in t:
            if not freq_arr[ord(char) - ord("a")]:
                return False

            freq_arr[ord(char) - ord("a")] -= 1

        return True
