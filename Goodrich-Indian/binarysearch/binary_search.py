def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid = (high+low)//2
        print(data,target,low,high)
        if data[mid]==target:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)


data,target,low,high= [1,2,3,4,5,6,7,8,9,10,11,12],4,0,5

print(binary_search(data,target,low,high))

