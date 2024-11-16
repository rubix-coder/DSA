"""
URL: https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in number_set:
                length = 0
                while (num + length) in number_set:
                    length += 1
                longest = max(longest, length)

        return longest

"""
Runtime
4246 ms Beats 28.35% of users with Python3
Memory
31.76 MB Beats 74.67% of users with Python3
"""