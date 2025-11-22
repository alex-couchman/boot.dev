class Trie:
    def search_level(self, current_level, current_prefix, words):
        for letter in sorted(current_level):
            if letter == self.end_symbol:
                words.append(current_prefix)
            else:
                self.search_level(current_level[letter], current_prefix + letter, words)
        return words
            

    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return words
            current = current[letter]
        return self.search_level(current, prefix, words)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True


import os
import json

if __name__ == "__main__":
    os.system('cls')
    trie = Trie()
    words = ['hi', 'help', 'hello']
    for word in words:
        trie.add(word)
    json_output = json.dumps(trie.root, indent=4, sort_keys=True)
    os.system('cls')
    print(json_output)

    print(trie.search_level(trie.root['h']['e'], 'he', []))
    print(trie.words_with_prefix('he'))