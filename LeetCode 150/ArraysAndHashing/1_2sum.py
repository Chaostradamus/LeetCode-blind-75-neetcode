class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in map:
                return map[diff], i
            map[n] = i

# o(n) time and space
# since we are gauranteed an answer, we know there exist a pair of numbers that will add up to target
# we take current iteration enumerated and subtract from target, if that difference is in the map
# we know we have encountered already and that pairs up with our current number
# we return the map[difference] value which is the index, and current i for current index
# else if diff is not in map, we add it to the hashmap by key = value of current iteration, and value = index of current

# example [2, 7, 11, 15] target = 9
# 9 - 2 = 7 first go thorugh and 7 doex not exist in map so we add key = 2 and value = index(0)
# 2nd iteration we do target - n again which is 9 - 7 = 2. this time 2 is in the hashmap
# so we can return i(1) and hashmap[difference] which is key = 2 which returns 0