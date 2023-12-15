import collections
import heapq
class Solution(object):

    class KthLargest(object):

        def __init__(self, k, nums):
            """
            :type k: int
            :type nums: List[int]
            """
            self.minny, self.k = nums, k
            heapq.heapify(self.minny)
            while len(self.minny) > k:
              heapq.heappop(self.minny)
        

        def add(self, val):
            """
            :type val: int
            :rtype: int
            """
    
            heapq.heappush(self.minny, val)
            if len(self.minny) > self.k:
              heapq.heappop(self.minny)
            return self.minny[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)







# https://pythontutor.com/render.html#code=import%20collections%0Aimport%20heapq%0Aclass%20Solution%28object%29%3A%0A%0A%20%20%20%20class%20KthLargest%28object%29%3A%0A%0A%20%20%20%20%20%20%20%20def%20__init__%28self,%20k,%20nums%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Atype%20k%3A%20int%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Atype%20nums%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%20%20%20%20self.minny,%20self.k%20%3D%20nums,%20k%0A%20%20%20%20%20%20%20%20%20%20%20%20heapq.heapify%28self.minny%29%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20len%28self.minny%29%20%3E%20k%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20heapq.heappop%28self.minny%29%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20def%20add%28self,%20val%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Atype%20val%3A%20int%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20heapq.heappush%28self.minny,%20val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20len%28self.minny%29%20%3E%20self.k%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20heapq.heappop%28self.minny%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20self.minny%5B0%5D%0A%0A%20%20%20%20%20%20%20%20%0A%0Ab%20%3D%20Solution%28%29%0Ab.KthLargest%283,%20%5B1,2,3,4,5%5D%29&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false