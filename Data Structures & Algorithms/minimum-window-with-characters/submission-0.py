from collections import defaultdict;
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s1 = defaultdict(int)
        for i in t:
            s1[i] += 1
        l = 0
        count = 0 
        min_len = float("inf")
        len_dict = dict()

        for r in range(len(s)):
            if s[r] in s1:
                s1[s[r]] -= 1
                if s1[s[r]] >= 0:
                    count += 1

            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    len_dict[min_len] = (l,r)

                if s[l] in s1:
                    s1[s[l]] += 1
                    if s1[s[l]] > 0:
                        count -= 1
                l += 1

        if min_len == float("inf"):
            return ""
        l,r = len_dict[min_len]
        return s[l:r+1]
