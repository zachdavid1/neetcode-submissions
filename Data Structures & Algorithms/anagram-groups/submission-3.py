class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output = []

        for word in strs:
            key = ''.join(sorted(word))
            if key in seen: 
                seen[key].append(word)
            else:
                seen[key] = [word]
            
        for value in seen.values():
            output.append(value)
        return output