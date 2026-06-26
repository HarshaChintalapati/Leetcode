class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for d in t:
            if d not in count or count[d] == 0:
                return d
            count[d] -= 1
        return ""

        
        