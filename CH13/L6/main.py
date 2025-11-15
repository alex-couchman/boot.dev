class Trie:
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
