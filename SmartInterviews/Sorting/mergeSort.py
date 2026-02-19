# Enter your code here. Read input from STDIN. Print output to STDOUT

# def merge(ar, low, mid, high):
#     temp= []
#     i = low
#     j = mid+1
#     k = 0

#     print('coming',low,mid,high)
#     while (i <= mid and j <= high):
#         if ar[i] < ar[j]:
#             temp.append(ar[i])
#             i += 1
#         else:
#             temp.append(ar[j])
#             j += 1

#     while i <= mid:
#         temp.append(ar[i])
#         i += 1

#     while j <= high:
#         temp.append(ar[j])
#         j += 1

#     print("temp",temp)

    # for i in range(len(temp)):
    #     ar[low+i] = temp[i]

def merge(ar,low,mid,high):

    left = ar[low:mid+1]
    right = ar[mid+1:high+1]

    i = 0
    j = 0
    k = low


    while(i<len(left) and j < len(right)):

        if left[i] < right[j]:
            ar[k] = left[i]
            print("1",ar[k],i,k,k-i)
            k += 1
            i += 1

        else:
            ar[k] = right[j]
            print("2",ar[k],j,k,k-j)
            j += 1
            k += 1

        
    while(i<len(left)):
        ar[k] = left[i]
        print("3",ar[k],i,k,k-i)
        k += 1
        i += 1

    while(j< len(right)):
        ar[k] = right[j]
        print("4",ar[k],j,k,k-j)
        k += 1
        j += 1


    # print('inside',ar)














def mergeSort(ar,low,high):

    count = 0

    if low<high:
        mid = (low+high)//2
        mergeSort(ar,low,mid)
        mergeSort(ar,mid+1,high)
        merge(ar,low,mid,high)



hashmap = {}
# a = [9,4,2,7,8,10,1,8,0,-5]
a = [4, 10, 54, 11, 8]

for i in range(len(a)):
    hashmap[a[i]] = i

print(hashmap)
print(a)
mergeSort(a,0,len(a)-1)
print(a)





def merge(ar, low, mid, high):

    i = low
    j = mid + 1
    temp = []
    count = 0

    while(i<=mid and j<=high):
        if ar[i]<=ar[j]:
            temp.append(ar[i])
            i += 1
        else:
            temp.append(ar[j])
            count += ((mid-i)+1)
            j += 1

    
    while(i<=mid):
        temp.append(ar[i])
        i += 1

    while(j<=high):
        temp.append(ar[j])
        j += 1

    for k in range(len(temp)):
        ar[low+k] = temp[k]
    return count

