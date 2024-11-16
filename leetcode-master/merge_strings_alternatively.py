"""
URL : https://leetcode.com/problems/merge-strings-alternately/description/

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i, j in zip(word1, word2):
            ans += i
            ans += j

        ans += word1[len(word2):]
        ans += word2[len(word1):]
        return ans
"""
Runtime
26 ms Beats 96.47% of users with Python3
Memory
16.50 MB Beats 93.54% of users with Python3
"""





class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        ans = ""
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return "".join(ans)

"""
Runtime
30 ms Beats 87.23% of users with Python3
Memory
16.61 MB Beats 12.27% of users with Python3
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        ans = ""
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return ans

"""
Runtime
23 ms Beats 98.71% of users with Python3
Memory
16.44 MB Beats 93.54% of users with Python3
"""