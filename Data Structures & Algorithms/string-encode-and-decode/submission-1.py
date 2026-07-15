class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            l = int(s[i:j])

            j += 1

            decoded_strings.append(s[j : j + l])
            i = j + l

        return decoded_strings
