"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letter
"""


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ref_dict = {}
        for i in s:
            if i in ref_dict:
                ref_dict[i] += 1
            else:
                ref_dict[i] = 1

        for j in t:
            if j in ref_dict:
                ref_dict[j] -= 1
            else:
                return False
        print(ref_dict)
        return not any(k != 0 for k in ref_dict.values())


"""
Runtime
52 ms Beats 41.94% of users with Python3
Memory
16.72 MB Beats 99.31% of users with Python3
"""
s = "aacc"
t = "ccac"

sol = Solution()
print(sol.isAnagram(s, t))



class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ref_dict = {}
        for i in s:
            if i in ref_dict:
                ref_dict[i] += 1
            else:
                ref_dict[i] = 1

        for j in t:
            if j in ref_dict and ref_dict[j] != 0:
                ref_dict[j] -= 1
            else:
                return False
        return not any(k != 0 for k in ref_dict.values())

"""
Runtime
44 ms Beats 80.49% of users with Python3
Memory
16.86 MB Beats 91.18% of users with Python3
"""


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ref_dict = {}
        for i in s:
            if i in ref_dict:
                ref_dict[i] += 1
            else:
                ref_dict[i] = 1

        for j in t:
            if j in ref_dict and ref_dict[j] != 0:
                ref_dict[j] -= 1
            else:
                return False
        return True

"""
Runtime
56 ms Beats 22.88% of users with Python3
Memory
16.86 MB Beats 91.18% of users with Python3
"""

class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter,0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter,0) + 1

"""
45ms Beats 76.79%
16.94MB Beats 43.51%
"""
