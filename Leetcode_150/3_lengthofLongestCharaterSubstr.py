#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        substr = set()
        l = 0

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength
    

    # O(N)
    # O(1)