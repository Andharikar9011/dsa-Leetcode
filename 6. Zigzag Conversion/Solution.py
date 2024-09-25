class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = ""
        if numRows == 1:
            return s
        if numRows >= 2:
            for i in range(numRows):
                step = (2*numRows) - 2
                if i == 0 or i == numRows-1:
                   
                    flag = 0
                    j = i
                    inc = 0
                    while j < len(s):
                        if flag == 0:
                            t+=s[j]
                            inc = step - (2*i)
                            j+= inc
                            flag=1
                        else:
                            t+=s[j]
                            j-=inc
                            j+= step
                            flag=0
            return t