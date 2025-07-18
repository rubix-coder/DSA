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
# def getNum(char):
#     if char == "0":
#         return 1
#     return -1

# def largestSubarraySum(myArray):
#     ans = 0
#     for i in myArray:
#         if i == "1":
#             ans+=1
#     maxSum = -sys.maxsize - 1
#     currSum = 0
#     subArray = []

#     for str_val in myArray:
#         currSum += getNum(str_val)
#         if currSum > maxSum:
#             maxSum = currSum
#             subArray.append(str_val)
#         if currSum < 0:
#             currSum = 0
#     return maxSum+ans,subArray

# myArray = input("Enter the binary string: ")
# print(largestSubarraySum(myArray))

# Provided by tutedude helpline
def kadaneAlgorithm(myArray):
    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0
    n = len(myArray)

    while end < n:
        # Add the current element to currSum
        currSum += myArray[end]
        # Update maxSum if currSum is larger
        maxSum = max(maxSum, currSum)
        # If currSum becomes negative, reset it and adjust start
        if currSum < 0:
            currSum = 0
            start = end + 1
        end += 1
    
    return maxSum


# myArray = [int(input(f"Enter number_{i}: ")) for i in range(int(input("Enter the array size: ")))]
# print(largestSubarraySum(myArray))

# @rubix-coder 2D kadane algo implementation
def kadane(arr):
    max_sum = -sys.maxsize - 1
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# def maxSumSubmatrix(matrix):
#     if not matrix:
#         return 0
#     else:
#         print(matrix)

#     rows = len(matrix)
#     cols = len(matrix[0])
#     max_sum = -sys.maxsize - 1

#     for top in range(rows):
#         print(f"top in range(rows) -> top@{top}")
#         temp = [0] * cols
#         print(f"temp [0]*cols -> {temp}\n")

#         for bottom in range(top, rows):
#             print(f"bottom in range(top,rows) -> bottom@{top,rows}")
#             for col in range(cols):
#                 print(f"col in range(cols) -> col@{col}")
#                 temp[col] += matrix[bottom][col]
#                 print(f"temp[col] += matrix[bottom][col] -> {temp}\n")

#             # Apply 1D Kadane on collapsed row pair
#             current_max = kadane(temp)
#             print(f"Current Max = kadane(temp) -> {current_max}")
#             max_sum = max(max_sum, current_max)
#             print(f"max_sum = max(max_sum, current_max) -> {max_sum}\n{'='*50}")

#     return max_sum

# Example usage
matrix = [
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6],
    [1, 2, -1, -4, -20],
]

matrix = [[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]


def jKadanesAlgo(matrix):
    lenRow = len(matrix)
    lenCol = len(matrix[0])

    # print(lenRow,lenCol)
    colSumArr = []
    for j in range(0,lenCol):
        colSum=0
        for i in range(0,lenRow):
            # print(f"matrix[{i}][{j}] -> {matrix[i][j]}")
            colSum+=matrix[i][j]
            # print(colSum)
        colSumArr.append(colSum)
        # print(colSumArr)
    return kadane(colSumArr)

print(jKadanesAlgo(matrix))
print("MATCH 100%") if kadane([-3,4,18,9,-4])==jKadanesAlgo(matrix) else print("NOT MACHING!")


# print("Maximum sum submatrix:", maxSumSubmatrix(matrix))
