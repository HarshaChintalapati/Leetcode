class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map={}
        nums=-1
        for i in arr:
            map[i]=1+map.get(i,0)
        for k,v in map.items():
            if(v==k):
                nums=max(nums,v)
        return nums
        
        
        
        
        
        