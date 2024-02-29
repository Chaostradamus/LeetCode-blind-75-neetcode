class TimeMap(object):

    def __init__(self):
      self.keyStore = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.keyStore:
          self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res , values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
          m = (l + r) // 2
          if values[m][1] <= timestamp:
            res = values[m][0]
            l = m + 1
          else:
            r = m - 1
        return res
    

    # binary search but with searching off hashmaps values
    #key value pairs foo: bar, 1...bar2, 2.....bar3, 3
    # perform binary search after only getting values off given key

#     981. Time Based Key-Value Store
# Medium
# Topics
# Companies
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".