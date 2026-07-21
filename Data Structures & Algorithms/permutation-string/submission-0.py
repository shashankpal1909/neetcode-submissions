from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        l = 0

        for ch in s1:
            freq_s1[ch] += 1

        for r in range(len(s2)):
            freq_s2[s2[r]] += 1

            if r - l + 1 == len(s1):
                is_valid = True

                for i in freq_s1.keys():
                    if freq_s1[i] != freq_s2[i]:
                        is_valid = False
                        break

                freq_s2[s2[l]] -= 1

                if is_valid:
                    return True

                l += 1

        return False
