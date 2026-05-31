class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = -1
        seen = {}
        max_len = 0
        most_frequent = 0
        while r < (len(s)-1):
            r +=1
            r_char = s[r]
            if r_char in seen:
                seen[r_char] +=1
                
            else:
                seen[r_char] = 1
            if seen[r_char]> most_frequent:
                most_frequent = seen[r_char]
            
            window_size = r - l + 1
            while (window_size - most_frequent) > k:
                l_char = s[l]
                if seen[l_char] ==1:
                    seen.pop(l_char)
                else:
                    seen[l_char]-=1
                l +=1
                most_frequent = max(seen.values())
                window_size = r - l + 1
            if window_size > max_len:
                max_len = window_size
        return max_len

                
            

