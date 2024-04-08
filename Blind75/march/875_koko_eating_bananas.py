class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1 , max(piles)
        res = r

        while l <= r:
        #   total time
          k = 0
        # k
          mid = (l+r) // 2
          for p in piles:
            k += math.ceil(float(p) / mid)
          if k <= h:
            r = mid -1
            res = min(res, mid)
          else:
            l = mid + 1
        return res
    
# binary search again with couple twists
# while we binary search through the imaginary array of hours set from 1 to max of piles
# we set it ranging from 1 to max of piles because at its loest it will be 1 per hr and highest will be the max value per hour
# loop through values in piles while dividing each pile by the hourly eating rate
# if and only if the total time is small than the total hours given in h, that is when we take that hourly rate as the res
# we keep track of lowest possible by doing min of res and current hourly rate
# also if the total hours is lower than the given total , then you do binary search
# to search for a lower rate move r to mid -1 and to search for a higher right we move left to mid + 1

# WE DONT NOT SET RES OUTSIDE OF THE INNER WHILE LOOP BECAUSE THEN IT WILL TAKE THE INCORRECT LOWER HOURLY RATES(MIDDLE)
# WE WANT TO SET THE RES TO THE HOURLY RATE ONLY WHEN THE TOTAL HOURS ARE UNDER THE GIVEN HOURS
    

# 875. Koko Eating Bananas
# Solved
# Medium
# Topics
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 