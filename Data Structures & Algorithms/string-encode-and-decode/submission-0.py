class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s + "#"

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []

        i = 0
        while i < len(s):
            str_len = ""
            string = ""

            while s[i] != "#":
                str_len += s[i]
                i += 1

            i += 1  # skip trailing #

            if len(str_len) != 0:
                string = s[i : i + int(str_len)]
                i = i + int(str_len)
            i += 1  # skip trailing #

            decoded_string.append(string)

        return decoded_string
