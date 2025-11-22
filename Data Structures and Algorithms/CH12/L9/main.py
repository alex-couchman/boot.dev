class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        threshold = .05
        size_multiplier = 10
        size = len(self.hashmap)
        if size == 0:
            self.hashmap.append(None)
            return
        load = self.current_load()
        if load < threshold:
            return
        else:
            temp = self.hashmap
            newHashMap = HashMap(len(temp) * size_multiplier)
            self.hashmap = newHashMap.hashmap
            for each in temp:
                if each != None:
                    key, value = each[0], each[1]
                    self.insert(key, value)

    def current_load(self):
        filled = 0
        size = len(self.hashmap)
        for each in self.hashmap:
            if each != None:
                filled += 1
        if size == 0:
            return 1
        else:
            return filled / size

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
