"""
URL: https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List
from collections import Counter

#solution by rubix-coder
class SolutiontopKFrequent:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        most_frequent = Counter(nums)
        return list(most_frequent.keys())[:k]

nums = [1,1,1,2,2,3]
k = 2
result = SolutiontopKFrequent.topKFrequent(nums=nums,k=k)
print(result)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        result = []
        for key, value in hash_map.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


"""
Runtime
91 ms Beats 44.40% of users with Python3
Memory
21.95 MB Beats 23.67% of users with Python3
"""
