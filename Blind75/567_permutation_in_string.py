class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
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
 