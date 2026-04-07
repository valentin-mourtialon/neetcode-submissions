class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t): return False
            sCounter, tCounter = {}, {}
            for i in range(len(s)):
                sCounter[s[i]] = sCounter[s[i]] + 1 if s[i] in sCounter else 1
                tCounter[t[i]] = tCounter[t[i]] + 1 if t[i] in tCounter else 1
            return sCounter == tCounter
        
        def sortString(s: str) -> str:
            return "".join(sorted(list(s)))
        
        res = []
        uniques = set()
        for i in range(len(strs)):
            sortedString = sortString(strs[i])
            if sortedString in uniques:
                continue
            if i == len(strs) - 1 and sortedString not in uniques:
                res.append([strs[i]])
                break
            uniques.add(sortedString)
            anagrams = [strs[i]]
            for j in range(i + 1, len(strs)):
                if isAnagram(strs[i], strs[j]):
                    anagrams.append(strs[j])
            res.append(anagrams)
        return res