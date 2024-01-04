class Solution(object):
    def checkInclusion(self, s1, s2):
        # length check. if s1 longer than s2 than there cannot exist a permutation ex: s1 = boob s2 = bo
        if len(s1) > len(s2):
          return False
        
        # create to arrays alphabet length size to hold counts
        s1c, s2c = [0] * 26, [0] * 26


# adding 1 to each count array going by length of s1 only
        for i in range(len(s1)):
          s1c[ord(s1[i]) -  ord("a")] += 1
          s2c[ord(s2[i]) -  ord("a")] += 1
# set matches variable and then go through entire alphabet and check for matches between the two arrays
        matches = 0
        for i in range(26):
          if s1c[i] == s2c[i]:
            matches += 1
# set left pointeron s2 
        l = 0
# will now go through with r iterator only length of s1 to end of s2 times. set beginniner to end of s1 because we already
        # added counts up to end of s1....we will check here for matches to be 26 which means permutation exists 
        for r in range(len(s1), len(s2)):
          if matches == 26:
            return True
# set index/letter to next letter after end of s1 length...thats why we start iterator there
        #   this emulates a sliding window using this as the right pointer
          index = ord(s2[r]) - ord("a")

# add a 1 to the s2count at new letter only because s1count is hardcoded at this point   
          s2c[index] += 1
# check for matches between count arrays at new letter/index add 1 if so and to csubtract one we will 
        #   check if adding 1 to s1count at index matches up...if so we subtract from MATCHES total
          if s1c[index] == s2c[index]:
            matches +=1
          elif s1c[index] + 1 == s2c[index]:
            matches -= 1
# next we go back to pop/slide left pointer by setting index to s2 at previous L pointer which starts at 0
            # remove a count from s2count array at new letter/index
          index = ord(s2[l]) - ord("a")
          s2c[index] -= 1
        #   redo checks
          if s1c[index] == s2c[index]:
            matches += 1
          elif s1c[index] +1 == s2c[index]:
            matches -= 1
            # move left pointer after checking
          l += 1
# finally out of that Rth iteration and return if everything matches else we go till end of s2 and return false
        return matches == 26
        

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20checkInclusion%28self,%20s1%3A%20str,%20s2%3A%20str%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20if%20len%28s1%29%20%3E%20len%28s2%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20%20%20%20%20s1Count,%20s2Count%20%3D%20%5B0%5D%20*%2026,%20%5B0%5D%20*%2026%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28s1%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20s1Count%5Bord%28s1%5Bi%5D%29%20-%20ord%28%22a%22%29%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bord%28s2%5Bi%5D%29%20-%20ord%28%22a%22%29%5D%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20matches%20%3D%200%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%2826%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%201%20if%20s1Count%5Bi%5D%20%3D%3D%20s2Count%5Bi%5D%20else%200%0A%0A%20%20%20%20%20%20%20%20l%20%3D%200%0A%20%20%20%20%20%20%20%20for%20r%20in%20range%28len%28s1%29,%20len%28s2%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20matches%20%3D%3D%2026%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%3D%20ord%28s2%5Br%5D%29%20-%20ord%28%22a%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bindex%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s1Count%5Bindex%5D%20%3D%3D%20s2Count%5Bindex%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20s1Count%5Bindex%5D%20%2B%201%20%3D%3D%20s2Count%5Bindex%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20-%3D%201%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%3D%20ord%28s2%5Bl%5D%29%20-%20ord%28%22a%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20s2Count%5Bindex%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s1Count%5Bindex%5D%20%3D%3D%20s2Count%5Bindex%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20s1Count%5Bindex%5D%20-%201%20%3D%3D%20s2Count%5Bindex%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matches%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20matches%20%3D%3D%2026%0A%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.checkInclusion%28%22ab%22,%20s2%20%3D%20%22eidbaooo%22%29&cumulative=false&curInstr=106&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# 567. Permutation in String
# Medium
# 10.9K
# 367
# Companies
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 