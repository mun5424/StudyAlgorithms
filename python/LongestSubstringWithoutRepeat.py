# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# "aabbccdd"

class Solution:
       def lengthOfLongestSubstring(self, s: str) -> int:
        letters = []
        n = len(s)
        i = 0
        j = 0
        ans = 0
        while (i < n and j < n):
            print(letters)
            if not s[j] in letters: 
                letters.append(s[j])
                ans = max(ans, j-i)
                j += 1
            else: 
                letters.remove(s[i])
                i +=1
        return ans

solution = Solution()
solution.lengthOfLongestSubstring("abcdeasdasd"); 