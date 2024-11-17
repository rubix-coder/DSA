"""
URL : https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_string = ""
        for i in s:
            if i.isalnum():
                alpha_string += i.lower()
        l = 0
        r = len(alpha_string) - 1
        while l < r:
            if alpha_string[l] != alpha_string[r]:
                return False
            l += 1
            r -= 1
        return True


"""
Runtime
46 ms Beats 50.93% of users with Python3
Memory
16.95 MB Beats 91.66% of users with Python3
"""


# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:

            while not s[l].isalnum() and l < r:
                l += 1

            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


"""
Runtime
50 ms Beats 29.74% of users with Python3
Memory
16.90 MB Beats 99.43% of users with Python3
"""

s = "race a car"
s = "a."
s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s))
