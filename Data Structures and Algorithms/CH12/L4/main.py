class HashMap:
    def key_to_index(self, key):
        unicode_sum = 0
        for char in key:
            unicode_sum += ord(char)
        index = unicode_sum % len(self.hashmap)
        return index

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
