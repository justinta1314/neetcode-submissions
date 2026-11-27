class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += str(len(s)) + "#" + s
        return final

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            i = start
            while s[i] != '#':
                i += 1
            length = int(s[start:i])
            word = s[i + 1:i + length + 1]
            res.append(word)
            start = i + length + 1
        return res