class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sCounter = {}
        tCounter = {}
        for i in range(len(s)):
            sCounter[s[i]] = 0 if s[i] not in sCounter else sCounter[s[i]] + 1
            tCounter[t[i]] = 0 if t[i] not in tCounter else tCounter[t[i]] + 1
        for letter, c in sCounter.items():
            if letter not in tCounter or tCounter[letter] != c:
                return False
        return True


        