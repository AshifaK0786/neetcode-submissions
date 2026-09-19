class Solution:
    def lengthOfLongestSubstring(self, s):
        sub=""
        ans=0
        for ch in s:
            if ch in sub:
                sub=sub[sub.index(ch)+1:]
            sub+=ch
            ans=max(ans,len(sub))
        return ans