"""
Url : https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

#  Solution by rubix-coder
class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!= len(nums)

"""
419 ms Beats 51.40%
31.95 MB Beats 44.45%
"""

from typing import List


# Solution 1
# Cons: Time limit exceeded
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrays = []

        for i in nums:
            if i not in arrays:
                arrays.append(i)
            else:
                return True
        return False


# Solution 2
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrays = set(nums)

        if len(arrays) == len(nums):
            return False
        return True


"""
Runtime
425 ms Beats 31.28% of users with Python3
Memory
31.98MB Beats 59.59% of users with Python3
"""


# Solution 3
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


"""
Runtime
466 ms Beats 5.07% of users with Python3
Memory
28.32 MB Beats 93.65 of users with Python3
"""


