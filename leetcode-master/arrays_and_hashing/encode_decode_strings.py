"""
Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

Example(s):

Example1

Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “lint:;code:;love:;you”

Example2

Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”] Explanation: One possible encode method is: “we:;say:;:::;yes”
"""

#solution by rubix-coder
import random
class SolutionEncodeDecode:

    def encode(strs):
        encoded_str = []
        for s in strs:
            encoded_str.append(f"{random.randint(0,len(s))}{s}{random.randbytes(3)}{random.choice(strs)}")
        return encoded_str

    def decode(strs):
        decoded_str = []
        for s in strs:
            decoded_str.append(f"{s.split("b'")[0][1:]}")
        return decoded_str
""
prompts = ["lint","code","love","you","algorithms","ML","!", "rubix", "coder"]



for _ in range(20,200):
    msg = [random.choice(prompts) for _ in range(1,random.randint(2,len(prompts)))]
    encoded = SolutionEncodeDecode.encode(strs=msg)
    print(f"encoded msg -> {encoded}")
    decode = SolutionEncodeDecode.decode(encoded)
    print(f"decoded msg -> {decode}\n############")

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


# s = Solution()
# input_list = ["python", "learning", "leet", "code"]
# encode_str = s.encode(input_list)
# print(encode_str)
# print(s.decode(encode_str))
