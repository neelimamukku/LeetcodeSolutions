import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = collections.defaultdict(int)
        c = 0
        for i in range(1,n+1):
            if i % 10 == 0:
                c = sum(map(int,str(i)))
                d[c] += 1
            else:
                c += 1
                d[c] += 1
        return list(d.values()).count(max(list(d.values())))
