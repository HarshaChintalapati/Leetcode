class Solution:
    def firstUniqChar(self, s: str) -> int:
        map={}
        for c in s:
            map[c]=1+map.get(c,0)
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1
        