class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
timeMap = TimeMap()

timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)
timeMap.get("foo", 3)
timeMap.set("foo","bar2", 4)
timeMap.get("foo", 4)
timeMap.get("foo", 5)

#     ["TimeMap","set","get","get","set","get","get"]
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]