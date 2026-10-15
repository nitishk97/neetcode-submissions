import bisect
class TimeMap:

    def __init__(self):
        self.map = {} # key: (timeMap, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        pairs = self.map[key] #[(1, alice),(2, happy)]
        index = bisect.bisect_right(pairs, (timestamp, chr(127)))
        if index==0:
            return ""
        return pairs[index-1][1]

