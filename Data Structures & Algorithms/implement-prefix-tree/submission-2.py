class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node['#'] = {}

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True


        