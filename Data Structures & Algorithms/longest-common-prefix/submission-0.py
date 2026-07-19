class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for idx in range(1, len(strs)):
            current_common = ""

            for i in range(min(len(common), len(strs[idx]))):
                if common[i] != strs[idx][i]:
                    break

                current_common += common[i]

            common = current_common

        return common
