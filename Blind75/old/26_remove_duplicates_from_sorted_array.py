class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0

        for r in range(len(nums)):
          if nums[r] != nums[r-1]:
            print(r)
            nums[l] = nums[r]
            l +=1
        return l
    

    # 2 pointer solution moving left adn right poiinters
    # check right pointer as you move along with r-1 cause you will run into duplicates in the list with l if not
    # checking l and r in place will get you duplicates but checking r with r-1 will not
        
