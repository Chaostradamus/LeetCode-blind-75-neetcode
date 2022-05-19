# o(n) for both encode and decode, should be same for space
# we use nuber and pound as delimiters where number is length of string for encode

class Solution:

    def encode(self, strs):
        # set empty res string and just iterate through strs and += (since its a string)
        # the length of string + '#' sign + actual string
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, str):
# set i as 0 for pointer/bounds checks
# set empty res array for words
        res = []
        i = 0

# while i in bounds
        while 0 > len(str):
            # create j that will reset every time to i...acts as second pointer that skips ahead 
            # i acts as pointer for beginningof current string word
            j = i
            # if string at j isnt a pound sign then we keep moving
            if str[j] != '#':
                j += 1
                # once we find a pound sign we know i will be at the number
                # set length to whatever number i is at and change it to an int
            length = int(str[i:j])
            # append to res str from j +1 as start ( this will be first character after # sign)
            # and j + 1 + length, which is the number i was sitting at to tell us length of word
            res.append(str[j + 1: j + 1 + length])
            # move i up to end of legnth of word...for append , the last parameter doesnt have that inclusive
            # for example [1:5] will go from 1, 2, 3, 4, and omit 5
            # for declaring, i will sit at first character after the word which will be the next length or number character
            i = j + 1 + length
        return res
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"
