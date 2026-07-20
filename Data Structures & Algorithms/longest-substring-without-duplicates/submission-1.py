class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, n = 0, 0, len(s)
        s_set = set()
        max_len = 0

        while j < n:
            while s[j] in s_set:
                s_set.remove(s[i])
                i += 1

            s_set.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len
