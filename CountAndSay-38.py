class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for j in range(n-1):
            r = ""
            c = 1
            i = 1
            for i in range(len(s)-1):
                if s[i+1] == s[i]:
                    c += 1
                else:
                    r += str(c)+s[i]
                    c = 1
            r += str(c)+s[len(s)-1]
            s = r
        return s
