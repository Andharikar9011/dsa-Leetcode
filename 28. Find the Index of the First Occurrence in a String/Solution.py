class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        if needle == "":
            return 0
        for i in range(n):
            if n-i >= len(needle):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1