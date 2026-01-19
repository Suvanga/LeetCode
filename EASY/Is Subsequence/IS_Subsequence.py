class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s.split()
        t.split()
        val =0
        i,j=0,0
        while i < len(s) and j< len(t):
            if s[i] == t[j]:
                i = i+1
            j= j+1
        if i == len(s):
            return True
        else:
            return False
