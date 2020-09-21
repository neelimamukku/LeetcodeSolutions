class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        even = []
        odd = []
        for i in A:
            e = "".join(sorted([i[x] for x in range(len(i)) if x % 2 == 0]))
            o = "".join(sorted([i[x] for x in range(len(i)) if x % 2 != 0]))
            even.append(e+o)
        print(even)
        return len(set(even))
