class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            final += str(len(word)) + "#" + word
        return final

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            i = start

            while s[i] != "#":
                i += 1
            length = int(s[start:i])
            word = s[i + 1:i + 1 + length]
            res.append(word)
            start = i + 1 + length
        return res