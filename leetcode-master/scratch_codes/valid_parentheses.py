"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


class Solution:
    def isValid(self, s) -> bool:
        parentheses_dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in parentheses_dict.values():
                stack.append(i)
            elif i in parentheses_dict.keys():
                if not stack or parentheses_dict[i] != stack.pop():
                    return False
        return not stack


"""
Runtime
37 ms Beats 46.32% of users with Python3
Memory
16.48 MB Beats 98.05% of users with Python3
"""

# x = []
# print(x.pop())

sol = Solution()
print(sol.isValid("]"))
