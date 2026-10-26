class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        for word in strs:
            for letter in word:
                code.append(str (ord(letter)))
                code.append(" ")
            code.append("!")
        
        res = ''.join(code)

        return res
            
    def decode(self, s: str) -> List[str]:
        
        string = []
        words = s.split('!')[:-1]
        res = []
        for word in words:
            letters = word.split(' ')[:-1]
            decoded = [chr(int(letter)) for letter in letters]
            res.append(''.join(decoded))

        return res
