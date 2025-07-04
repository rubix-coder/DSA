# Kadane Algorithm -> Find the maxSum subarray
import sys

# def largestSubarraySum(myArray):
#     maxSum= -sys.maxsize -1
#     currSum=0
#     start=0
#     end=0
#     n = len(myArray)

#     while end < n:
#         while currSum < 0:
#             currSum -=myArray[start]
#             start+=1

#         currSum -=myArray[end]
#         end+=1
#         maxSum = max(maxSum,currSum)
#     return maxSum

# myArray = [int(input(f"Enter number_{i}: ")) for i in range(int(input("Enter the array size: ")))]
# print(largestSubarraySum(myArray))

# @rubix-coder: Kadane Algorithm Method 2
#=================================================
# def largestSubarraySum(myArray):
#     maxSum = -sys.maxsize - 1
#     currSum = 0
#     subArray = []

#     for num in myArray:
#         currSum += num
#         if currSum > maxSum:
#             maxSum = currSum
#             subArray.append(num)
#         if currSum < 0:
#             currSum = 0
#     return maxSum,subArray

# myArray = [int(input(f"Enter number_{i}: ")) for i in range(int(input("Enter the array size: ")))]
# print(largestSubarraySum(myArray))

#@rubix-coder FLIPBITS modified code
#=================================================
def getNum(char):
    if char == "0":
        return 1
    return -1

def largestSubarraySum(myArray):
    ans = 0
    for i in myArray:
        if i == "1":
            ans+=1
    maxSum = -sys.maxsize - 1
    currSum = 0
    subArray = []

    for str_val in myArray:
        currSum += getNum(str_val)
        if currSum > maxSum:
            maxSum = currSum
            subArray.append(str_val)
        if currSum < 0:
            currSum = 0
    return maxSum+ans,subArray

myArray = input("Enter the binary string: ")
print(largestSubarraySum(myArray))