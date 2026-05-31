class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) == len(t):
            for letter in s:
                if letter in seen:
                    seen[letter]+=1
                else:
                    seen[letter] = 1
            for letter in t:
                if letter in seen:
                    if seen[letter] == 1:
                        seen.pop(letter)
                    else:
                        seen[letter] -=1
                else:
                    break
            if len(seen) == 0:
                return True
        
        return False
        

            