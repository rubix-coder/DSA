"""
URL: https://leetcode.com/problems/two-sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# Solution 1 : Brute Force
nums = [2, 7, 11, 15]
target = 9

# Solution by rubix-coder:
class Solution_3:
    def twoSum(nus, target):
        cleaned = []
        for i in nus:
            if i <= target:
                cleaned.append(i)
        for i in cleaned:
            if target-cleaned[i] in cleaned:
                return [nus.index(cleaned[i]), nus.index(target-cleaned[i])]


sol_3 = Solution_3.twoSum(nus = [1, 2, 3, 6], target = 9)
print(sol_3)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            expected = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == expected:
                    return ([i, j])

        return []


"""
================= Results ====================================
Runtime
947 ms
Beats 35.72% of users with Python3
================================
Memory
17.41 MB
Beats 65.07% of users with Python3
"""


# Solution 2 : One Pass Hash Table
class Solution_2:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in hash_map:
                return [hash_map[num], i]
            hash_map[complement] = i
        return []


obj = Solution_2()
ans = obj.twoSum([2, 7, 11, 15], 9)
# print(ans)

"""
================= Results ====================================
Runtime
61 ms
Beats 57.44% of users with Python3
================================
Memory
18.12 MB
Beats 6.37% of users with Python3
"""

