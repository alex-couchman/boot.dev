class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return current.get(self.end_symbol, False)

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

import os
import json

if __name__ == "__main__":
    os.system('cls')
    trie = Trie()
    words = ['hi', 'hello', 'help']
    for word in words:
        trie.add(word)
    json_output = json.dumps(trie.root, indent=4, sort_keys=True)
    os.system('cls')
    print(json_output)

    print(trie.exists('hello'))
    print(trie.exists('he'))