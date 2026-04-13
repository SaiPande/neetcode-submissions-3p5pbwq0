class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        for pair in self.bucket[idx]:
            if key == pair[0]:
                pair[1] = value
                return    
        self.bucket[idx].append([key, value])    

    def get(self, key: int) -> int:
        idx = key % self.size
        for pair in self.bucket[idx]:
            if key == pair[0]:
                return pair[1]      
        return -1  


    def remove(self, key: int) -> None:
        idx = key % self.size
        for pair in self.bucket[idx]:
            if key == pair[0]:
                self.bucket[idx].remove(pair)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)