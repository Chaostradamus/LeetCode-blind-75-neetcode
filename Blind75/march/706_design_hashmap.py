class ListNode:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = None


class MyHashMap:

    def __init__(self):
      self.map = [ListNode() for i in range(1000)]
        
    def hash(self, key):
      return key % len(self.map)


    def put(self, key: int, value: int) -> None:
      cur = self.map[self.hash(key)]
      while cur.next:
        if cur.next.key == key:
          cur.next.val = value
          return
        cur = cur.next
      cur.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
      cur = self.map[self.hash(key)].next
      while cur:
        if cur.key == key:
          return cur.val
        cur = cur.next
      return -1
                 

    def remove(self, key: int) -> None:
      cur = self.map[self.hash(key)]
      while cur and cur.next:
        if cur.next.key == key:
          cur.next = cur.next.next
          return
        cur = cur.next


# create listNode with key value and next
# init a hashmap array with listnodes at size length of constraint which is 1000 here
# creat ehelper function which hashes the key by doing key modulo length of map which is 1000
# to put something we set current pointer to map at current hashed key (if it exists) is next
# while there is a cur.next(we are inside the hashed index values  of listnodes now)
    # if the cur.next key matches then it already exists so we just set the value to val and return out
        # if not we go to cur.next until we find matching key
        # if we dont find a matchign key we will create a new one
# for get we get current pointer and while loop through and return if cur.vkey matches we return the cur.val 
#   if we dont find it then we return -1
# for remove we set the current pointer again and while theres a cur and a cur.next...we need cur,next so we dont run out of bounds when we 
#       set the .next.next for removal
#       we find matching keys..if we find one we remove the point by setting it to ,next.next

      
        

# 706. Design HashMap
# Easy
# Topics
# Companies
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 