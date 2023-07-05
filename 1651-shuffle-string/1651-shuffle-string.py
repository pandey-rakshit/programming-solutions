class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str = ''
        for i in range(len(s)):
            j = indices.index(i)
            str += s[j]
        return str