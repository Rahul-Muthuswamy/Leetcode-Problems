class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        l=[]
        for i in words:
            c=''
            for j in i:
                c+=d[j]
            l.append(c)
        s=set(l)
        return len(s)