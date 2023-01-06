class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        ne = 0
        g.sort()
        s.sort()

        for i in range(len(s)):
            for j in range(ne, len(g)):
                if g[j] <= s[i]:
                    cnt +=1
                    ne = j +1
                    break

        return cnt
        