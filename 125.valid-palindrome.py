#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([char.lower() for char in s if char.isalnum()])
        for i in range(len(cleaned_s) //2):
            if cleaned_s[i] != cleaned_s[len(cleaned_s)- 1 - i]:
                return False
        return True
# @lc code=end

