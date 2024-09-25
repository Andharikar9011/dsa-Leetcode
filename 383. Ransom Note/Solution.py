class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for i in magazine:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
        for i in ransomNote:
            if d.get(i) == None or d.get(i) == 0 :
                return False
            else:
                d[i]-=1
        return True   