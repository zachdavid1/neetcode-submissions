class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for element in s:
            if element in seen:
                seen[element]+=1
            else:
                seen[element] = 1
        
        for element in t:
            if element in seen:
                if seen[element] == 1:
                    seen.pop(element)
                else:
                    seen[element] -=1
            
            else:
                return False
        if len(seen)==0:
            return True
        return False
            
