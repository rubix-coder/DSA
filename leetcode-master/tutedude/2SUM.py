#@rubix-coder 2SUM problem
# Given an array and the target, find the subarray with 2 elements such that
# their sum is equal to the target

def solve2Sum(myArr, target):
    myArr = sorted(myArr)
    startPtr=0
    endPtr=len(myArr)-1

    while startPtr < endPtr:
        currSum = myArr[startPtr] + myArr[endPtr]
        if currSum == target:
            return f"{([myArr[startPtr],myArr[endPtr]])} at index {([startPtr,endPtr])}.\n"
        if currSum > target:
            endPtr-=1
        if currSum < target:
            startPtr+=1
    return -1
        
if __name__=='__main__':
    myArr = [int(input(f"Enter the element_{i}: ")) \
             for i in range(int(input("Enter the array size: ")))]
    target = int(input("Enter the target value: "))
    print(solve2Sum(myArr,target))