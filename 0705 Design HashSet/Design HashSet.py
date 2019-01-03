class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemPerBucket = 1000
        self.table = [[] for _ in range(self.buckets)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hashCalculate(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemPerBucket  # [0]*2:[0,0]
        self.table[hashkey][self.position(key)] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hashCalculate(key)
        if self.table[hashkey]:
            self.table[hashkey][self.position(key)] = 0

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hashCalculate(key)
        return (self.table[hashkey] != []) and (self.table[self.hashCalculate(key)][self.position(key)] == 1)

    def hashCalculate(self, key):
        return key % self.buckets

    def position(self, key):
        return key // self.buckets

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)