class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0 
        p2 = 0
        slen = len(s)-1
        tlen = len(t)-1
        counter = -1
        if slen>tlen:
            return False
        else:
            while p1 <= slen and p2 <= tlen:
                if s[p1] == t[p2]:
                    p1+=1
                    p2+=1
                    counter +=1
                else:
                    p2+=1
            if counter ==slen:
                return True 
            else:
                return False
        