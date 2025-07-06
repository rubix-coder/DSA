#@rubix-coder 2SUM problem
# Given an array and the target, find the subarray with 2 elements such that
# their sum is equal to the target

def solve2Sum(myArr, target):
    
    myArrSorted = sorted(myArr)
    startPtr=0
    endPtr=len(myArrSorted)-1
    listSubArray = []
    while startPtr < endPtr:
        currSum = myArrSorted[startPtr] + myArrSorted[endPtr]
        if currSum == target:
            listSubArray.append(([myArrSorted[startPtr],myArrSorted[endPtr]]))
            print(f"{([myArrSorted[startPtr],myArrSorted[endPtr]])} at index {([myArr.index(myArrSorted[startPtr]),myArr.index(myArrSorted[endPtr])])}.\n")
            if len(listSubArray)>0:
                startPtr+=1
                endPtr-=1
        if currSum > target:
            endPtr-=1
        if currSum < target:
            startPtr+=1
    try:
        return listSubArray
    except:
        return -1
        
if __name__=='__main__':
    myArr = [int(input(f"Enter the element_{i}: ")) \
             for i in range(int(input("Enter the array size: ")))]
    target = int(input("Enter the target value: "))
    solve2Sum(myArr,target)