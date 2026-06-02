class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = -1
        if not s:
            return 0
        seen = set()
        max_len = 0
        
        while r < len(s) -1:
            r +=1
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
        return max_len



            
        