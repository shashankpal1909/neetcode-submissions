class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i, j, n = 0, 0, len(s)
        s_set = set()
        max_len = 0

        while j < n:
            while j < n and s[j] not in s_set:
                s_set.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1

            while i < j and j < n:
                s_set.remove(s[i])
                if s[i] == s[j]:
                    i += 1
                    break
                i += 1

        return max_len
