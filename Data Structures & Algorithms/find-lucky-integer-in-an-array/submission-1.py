class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map={}
        max_num=-1
        for i in range(len(arr)):
            map[arr[i]]=1+map.get(arr[i],0)
        for k,v in map.items():
            if(v==k):
                max_num=max(max_num,v)
        return max_num       
        
        
        
        
        
        