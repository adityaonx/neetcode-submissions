class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        for i in range(len(s)):
            char_set=set()
            for j in range(i,len(s)):
                if s[j] in char_set:
                    break
                else:
                    char_set.add(s[j])
            max_len=max(max_len,len(char_set))
        return max_len





