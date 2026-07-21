class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, n = 0, 0, len(s)
        char_map = defaultdict(int)

        max_len = 0
        while j < n:
            # increase sliding window
            char_map[s[j]] += 1

            # shrink sliding window till it becomes valid
            while (j - i + 1) - max(char_map.values(), default=0) > k:
                char_map[s[i]] -= 1
                i += 1

            # calculate max window length
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len
