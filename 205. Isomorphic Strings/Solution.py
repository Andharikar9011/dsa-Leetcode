class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a1 =''
        b1 =''
        d1= dict()
        d2 = dict()
        c1 = 1
        c2 = 1
        if len(s) != len(t):
            return False
            # print(False)
        else:
            for i in range(len(s)):
                if d1.get(s[i]) == None:
                    d1[s[i]] = str(c1)
                    a1+=str(c1)
                    c1+=1
                else:
                    a1+= d1[s[i]]
                if d2.get(t[i]) == None:
                    d2[t[i]] = str(c2)
                    b1+=str(c2)
                    c2+=1
                else:
                    b1+= d2[t[i]]
            if a1 == b1:
                return True
                # print(True)
            else:
                return False
                # print(False)