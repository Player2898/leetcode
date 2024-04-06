class Solution:
    def makeGood(self, s: str) -> str:
        good = []
        for letter in s:
            good.append(letter)

            if len(good) >= 2 and good[-1].upper() == good[-2].upper() and good[-1] != good[-2]: #if any two bad adjacent characters appear together we pop them both 
                good.pop()
                good.pop()

        return "".join(good)

