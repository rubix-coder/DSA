"""
Url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""


# Solution 1: Two pointer solution

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            elif total < target:
                left += 1

        return []


"""
Runtime
109 ms
Beats 33.80% of users with Python3
Memory
17.51 MB
Beats 25.63% of users with Python3
"""


#  Solution 2: Hash map solution

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        hash_map = {}

        for i, num in enumerate(numbers):
            if num in hash_map:
                return [hash_map[num] + 1, i + 1]
            hash_map[target - num] = i


"""
Runtime
95 ms
Beats 95.33% of users with Python3
Memory
17.47 MB
Beats 57.96% of users with Python3
"""
