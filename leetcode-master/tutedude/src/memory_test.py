#kadane algorithm
# find the maxSum of a subArray from given array

import sys

# def maxSumSubArray(myArr):
#     maxSum=-sys.maxsize -1
#     currSum = 0
#     subArray = []
#     for num in myArr:
#         currSum+=num
#         if currSum>maxSum:
#             maxSum=currSum
#             subArray.append(num)
#         elif currSum<0:
#             currSum=0
#         else:
#             subArray.append(num)

#         maxSum = max(currSum,maxSum)
#     return maxSum,subArray[:-1]

# myArr = [int(input(f"Enter number_{idx}: ")) for idx in range(int(input("Enter array length: ")))]

# print(maxSumSubArray(myArr))


# Kadane modified for flipbits

def getNum(string_num):
    if string_num=="0":
        return 1
    else:
        return -1
    
def flipBits(myArr):
    ans=0
    for chr in myArr:
        if chr=="1":
            ans+=1
    maxSum=-sys.maxsize -1
    currSum = 0
    subArray = []
    for num in myArr:
        currSum+=getNum(num)
        if currSum>maxSum:
            maxSum=currSum
            subArray.append(num)
        elif currSum<0:
            currSum=0
        else:
            subArray.append(num)

        maxSum = max(currSum,maxSum)
    return maxSum+ans,subArray[:-1]

myArr = input("Enter the binary string: ")

print(flipBits(myArr))


    