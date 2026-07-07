class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        maxi = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxi = max(maxi, count[s[right]])

            while (right - left + 1) - maxi > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans