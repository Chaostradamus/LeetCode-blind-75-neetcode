class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {} , {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countS.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get([c], 0):
                return False
        
        return True

# o(n) time and space
# check if lenths are diff bc that signifies non anagram
# populate countS and countT hashmps with each letter from s and t. use.get(index, value) for zeroing error
# compare each c in countS, which i think is each key not character, compare to countT of same key
# non match will equal non anagram 
# return true if we get thourhg the checks