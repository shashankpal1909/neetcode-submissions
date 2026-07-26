class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid():
            for _, v in t_map.items():
                if v > 0:
                    return False
            return True

        i, j, n = 0, 0, len(s)
        t_map = Counter(t)
        res, min_len = "", len(s)

        while j < n:
            while j < n and not is_valid():
                if s[j] in t_map:
                    t_map[s[j]] -= 1
                j += 1

            while i < j and is_valid():
                if len(s[i:j]) - 1 < min_len:
                    min_len = len(s[i:j]) - 1
                    res = s[i:j]
                if s[i] in t_map:
                    t_map[s[i]] += 1
                i += 1

        while i < j and is_valid():
            if len(s[i:j]) - 1 < min_len:
                min_len = len(s[i:j]) - 1
                res = s[i:j]
            if s[i] in t_map:
                t_map[s[i]] += 1
            i += 1

        return res
