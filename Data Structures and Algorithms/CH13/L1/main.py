class Trie:
    def add(self, word):
        level = self.root
        for char in word:
            if char not in level:
                level[char] = {}
            level = level[char]
        level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


import json
import os

if __name__ == "__main__":
    os.system('cls')
    trie = Trie()
    words = ['hi', 'hello', 'help']
    for word in words:
        trie.add(word)
        json_output = json.dumps(trie.root, indent=4, sort_keys=True)
        os.system('cls')
        print(json_output)
        input('Any key to continue.\n')
