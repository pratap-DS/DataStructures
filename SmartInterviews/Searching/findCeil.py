def findCeil(array, element):
    k = len(array)-1
    low = 0
    high = k

    result = -1

    while(low<=high):
        m = (low+high)//2
            

        if array[m] == element:
            result = m
            low = m+1
        elif element < array[m]:
            high = m-1

        elif element > array[m]:
            low = m+1

    if result != -1:
        return result

    if low > k:
        return k+2

    return low

# print(findCeil([-2,0,1,3,5,7],-1))
# print(findCeil([-2,0,1,3,5,7],2))
# print(findCeil([-2,0,1,3],-50))
# print(findCeil([-2,0,1,3],5))
# print(findCeil([-2,0,0,0,0,0,0,1,3],-1))


def findFloor(array, element):

    k = len(array)-1
    low = 0
    high = k
    result = -1

    while(low<=high):
        m = (low+high)//2

        if array[m] == element:
            result = m
            low = m+1

        elif element < array[m]:
            high = m-1

        elif element > array[m]:
            low = m+1

    if result != -1:
        return result

    if high < 0:
        return -1
    
    return high

print(findFloor([-2,0,1,3,5,7],-1))
print(findFloor([-2,0,1,3,5,7],2))
print(findFloor([-2,0,1,3],-50))
print(findFloor([-2,0,1,3],5))
print(findFloor([-2,0,0,0,0,0,0,1,3],0))
