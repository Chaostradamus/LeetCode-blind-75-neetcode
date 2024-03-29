class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

      #   countS, countT = {}, {}
      # for i, n in enumerate(s):
      #   countS[n] = 1 + countS.get(n, 0)
      # for i, n in enumerate(t):
      #   countT[n] = 1 + countT.get(n, 0)
      # for c in countS:
      #     if countS[c] != countT.get(c, 0):
      #       return False
      # return True

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# explanation
# loop through S amount of times and add each character into hashmaps
# in python use .get to get the key if it doesnt exist yet with default value of 0
# interate through each hashmap by key s[c] and if not equal then return false
# in python use .get here to get key with default value of 0 so it doesnt throw an indexing error
# will be o(s + t) where s and t are length of string and space will be same
# can do better in space if you sort and compare but that will add time 

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20isAnagram%28self,%20s%3A%20str,%20t%3A%20str%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20if%20len%28s%29%20!%3D%20len%28t%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20%20%20%20%20countS,%20countT%20%3D%20%7B%7D,%20%7B%7D%0A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20countS%5Bs%5Bi%5D%5D%20%3D%201%20%2B%20countS.get%28s%5Bi%5D,%200%29%0A%20%20%20%20%20%20%20%20%20%20%20%20countT%5Bt%5Bi%5D%5D%20%3D%201%20%2B%20countT.get%28t%5Bi%5D,%200%29%0A%20%20%20%20%20%20%20%20return%20countS%20%3D%3D%20countT%0A%0Aleetcode%20%3D%20Solution%28%29%0Aleetcode.isAnagram%28%22dog%22,%20%22dog%22%29&cumulative=false&curInstr=18&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
# added own leetcode answer with enumerate