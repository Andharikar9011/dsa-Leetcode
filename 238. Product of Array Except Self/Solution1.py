class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        c = 1
        n = len(s)
        sc = 0
        counter = 0
        while c == 1 and n > 0:
            if s[n-1] == " " and sc !=1 :
                n-=1  
                continue
            elif s[n-1] == " " and sc ==1:
                c = 2
            else:
                n-=1
                sc=1
                counter +=1
        return counter