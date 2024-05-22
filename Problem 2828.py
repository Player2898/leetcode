class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) == len(s):   #if both the lengths are not equal then it cant form an acronym.
            for i in range(len(words)):
                if words[i][0] == s[i]: #first letter of the word[i] and each character in the string must be the same ex: words = ['attack','on'] s = 'ao'.
                    pass
                else:
                    return False
            return True
        return False
