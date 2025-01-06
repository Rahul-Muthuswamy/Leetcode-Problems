class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet={}
        k = 0
        for c in key:
            if c != ' ' and c not in alphabet:
                alphabet[c] = chr(k + ord('a'))
                k += 1
        decode = []
        for c in message:
            if c != ' ':
                decode.append(alphabet[c])
            else:
                decode.append(' ')
        return ''.join(decode)
            
