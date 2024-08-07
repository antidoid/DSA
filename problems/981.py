"""
Time Based Key-Value Store

Design a time-based key-value data structure that can store 
multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key 
key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that 
set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the 
largest timestamp_prev. If there are no values, it returns "".
"""

class TimeMap:
    def __init__(self):
        self.data = dict()

    # the list for each key will be sorted as the timestamps given
    # are in strictly increasing order
    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))
        

    # Time: O(log(n))
    # def get(self, key: str, timestamp: int) -> str:
    #     res = ""
    #
    #     ls = self.data.get(key, [])
    #     maxTimeLessThanTimestamp = 0
    #
    #     l, r = 0, len(ls) - 1
    #     while l <= r:
    #         m = (l + r) // 2
    #         if ls[m][1] == timestamp:
    #             return ls[m][0]
    #         elif ls[m][1] < timestamp:
    #             if ls[m][1] > maxTimeLessThanTimestamp:
    #                 maxTimeLessThanTimestamp = ls[m][1]
    #                 res = ls[m][0]
    #             l = m + 1
    #         else:
    #             r = m - 1
    #
    #     return res
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        ls = self.data.get(key, [])

        l, r = 0, len(ls) - 1
        while l <= r:
            m = (l + r) // 2
            if ls[m][1] <= timestamp:
                res = ls[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
