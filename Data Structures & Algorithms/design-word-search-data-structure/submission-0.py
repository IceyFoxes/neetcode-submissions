class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node['#'] = {}

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node

            letter = word[i]
            if letter == '.':
                for key, child in node.items():
                    if key != '#' and dfs(child, i + 1):
                        return True
                return False  # Every branch failed

            return letter in node and dfs(node[letter], i + 1)

        return dfs(self.root, 0)