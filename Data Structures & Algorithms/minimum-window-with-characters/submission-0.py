class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        ans = ""

        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1

                ok = True
                for ch in need:
                    if freq.get(ch, 0) < need[ch]:
                        ok = False
                        break

                if ok:
                    if ans == "" or (j - i + 1) < len(ans):
                        ans = s[i:j+1]
                    break

        return ans