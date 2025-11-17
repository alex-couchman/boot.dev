class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        current = self.root
        word = ""
        
        for char in document:
            if char in variations:
                char_alt = variations[char]
            else:
                char_alt = char
                
            if char_alt in current:
                word += char
                current = current[char_alt]
                if self.end_symbol in current:
                    matches.add(word)
            else:
                word = ""
                current = self.root
        return matches

    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        current = self.root
        word = ""
        for char in document:
            if char in current:
                word += char
                current = current[char]
                if self.end_symbol in current:
                    matches.add(word)
            else:
                word = ""
                current = self.root
        return matches

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
    trie = Trie()
    words_lst = ["darnit", "nope", "bad"]
    document = "This is a d@rn1t test with b@d words!"
    variations = {
                    "@": "a",
                    "1": "i",
                    "4": "a",
                    "!": "i",
                }

    for each in words_lst:
        trie.add(each)
    json_output = json.dumps(trie.root, indent=4, sort_keys=True)
    os.system('cls')
    print(json_output)
    matches = trie.advanced_find_matches(document, variations)
    print(matches)
