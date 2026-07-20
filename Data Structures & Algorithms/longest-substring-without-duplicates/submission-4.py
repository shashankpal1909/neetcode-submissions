class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, n = 0, 0, len(s)
        s_map = dict()
        max_len = 0

        while j < n:
            if s[j] in s_map.keys():
                # s_map[s[j]] may be out of our working window 
                # so we choose only if > i
                i = max(s_map[s[j]] + 1, i)

            s_map[s[j]] = j
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len
