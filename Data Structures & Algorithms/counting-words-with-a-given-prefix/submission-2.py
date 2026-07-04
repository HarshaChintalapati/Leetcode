class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output = 0
        pref_len = len(pref)
        
        for word in words:
            if word[:pref_len] == pref:
                output += 1
                
        return output



                
            
        