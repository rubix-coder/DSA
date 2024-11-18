"""
URL: https://leetcode.com/problems/product-of-array-except-self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

#Solution by rubix-coder
class SolutionProductOfTwoArray:
    def productExceptSelf(nums: List[int]) -> List[int]:
        product = 1
        result = []
        curated_list = nums[:]

        for i in range(0,len(nums)):
            curated_list = nums[:]
            curated_list.pop(i)
            for i in curated_list:
                product *= i
            result.append(product)
            product = 1   
        return result

SolutionProductOfTwoArray.productExceptSelf([1,2,3,4])



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        total_zeros = 0

        for i in nums:
            if i != 0:
                total_product *= i
            else:
                total_zeros += 1

        if total_zeros > 1:
            return [0] * len(nums)

        result = []
        for num in nums:
            if num != 0:
                if total_zeros == 1:
                    result.append(0)
                else:
                    result.append(total_product // num)
            else:
                result.append(total_product)
        return result

"""

Runtime
252 ms Beats 96.56% of users with Python3
Memory
25.56 MB Beats 94.32% of users with Python3
"""