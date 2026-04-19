class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        for i in range(len(s)):
            char_Set=set()
            for j in range(i,len(s)):
                if s[j] not in char_Set:
                    char_Set.add(s[j])
                else:
                    break
            max_len=max(max_len,len(char_Set))
        return max_len
