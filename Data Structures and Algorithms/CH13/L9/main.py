class Trie:
    def longest_common_prefix(self):
        current  = self.root
        prefix = ""
        while True:
            keys = list(current.keys())
            if self.end_symbol in keys or len(keys) != 1:
                break
            prefix += keys[0]
            current = current[keys[0]]
        return prefix

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


import os
import json

if __name__ == "__main__":
    names = ["Jerry", "Jess", "Jeremy"]
    trie = Trie()
    for each in names:
        trie.add(each)
    json_output = json.dumps(trie.root, indent=4, sort_keys=True)
    os.system('cls')
    print(json_output)
    prefix = trie.longest_common_prefix()
    print(prefix)