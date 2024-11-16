"""
Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

Example(s):

Example1

Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “lint:;code:;love:;you”

Example2

Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”] Explanation: One possible encode method is: “we:;say:;:::;yes”
"""


class Solution:

    def encode(self, strs):
        encode_str = ""
        for s in strs:
            encode_str += f"{len(s)}#{s}"
        return encode_str

    def decode(self, str):
        result = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


s = Solution()
input_list = ["sachin", "jose", "python", "learning", "leet", "code"]
encode_str = s.encode(input_list)
print(encode_str)
print(s.decode(encode_str))
