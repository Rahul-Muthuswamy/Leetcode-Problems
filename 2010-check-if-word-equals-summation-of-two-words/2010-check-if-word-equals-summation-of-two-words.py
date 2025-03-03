class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def find_num_of_word(word):
            str1 = ""
            for i in range(len(word)):
                str1 += str(ord(word[i]) - ord('a')) 
            return int(str1)  
        
        num1 = find_num_of_word(firstWord)
        num2 = find_num_of_word(secondWord)
        num3 = find_num_of_word(targetWord)

        return num1 + num2 == num3