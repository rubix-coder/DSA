"""
URL: https://leetcode.com/problems/group-anagrams/

"""
from collections import defaultdict
from typing import List


# Solution 1:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            result[tuple(count)].append(s)

        return result.values()


"""
Runtime
88 ms Beats 64.27% of users with Python3
Memory
22.37 MB Beats 13.37% of users with Python3
"""


# Solution 2: Failed approach
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = []
        for i in range(len(strs)):
            if strs[i] not in seen:
                anagram_list = [strs[i]]
                seen.append(strs[i])
                for j in range(1, len(strs)):
                    if strs[j] not in seen and self.find_anagram(strs[i], strs[j]):
                        anagram_list.append(strs[j])
                        seen.append(strs[j])
                result.append(anagram_list)
        return result

    def find_anagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        hash_map = {}
        for i in str1:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        for i in str2:
            if i in hash_map and hash_map[i] >= 0:
                hash_map[i] -= 1
            else:
                return False
        return True
