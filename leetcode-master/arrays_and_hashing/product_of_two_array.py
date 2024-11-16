"""
URL: https://leetcode.com/problems/product-of-array-except-self
"""

from typing import List
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