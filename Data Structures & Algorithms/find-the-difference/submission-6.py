class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map={}
        for a in t:
            map[a]=1+map.get(a,0)
        for b in s:
            map[b]=map.get(b,0)-1
        for k,v in map.items():
            if v==1:
                return k
        return ""
            



        
        