from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#" :
                j += 1
            length = int(s[i:j])
            i = j+1
            j = length+i
            res.append(s[i:j])
            i = j
        return res

sol = Solution()
encode_sol = sol.encode(["neet","code","love","you"])
print("encode_sol: ", encode_sol)
decode_sol = sol.decode(encode_sol)
print("decode_sol: ", decode_sol)
