class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_s = [x for x in s]
        print(letters_in_s)
        if len(s) != len(t):
            return False
        else:
            for letter in t:
                if letter not in letters_in_s:
                    return False
                else:
                    letters_in_s.remove(letter)
        return True

