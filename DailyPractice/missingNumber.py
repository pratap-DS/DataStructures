
def missingNumber(nums):

    """
        we should find the missing number in the given array ranges from 0 to n. where 0 is the missing number.
        hint: XOR of two lists, one is the given and the other is the numbers from 1 to n
    """
    
    result = 0
    for i in range(1,len(nums)+1):
        # i is the number from our array, nums[i-1] is the number from given array
        result = result ^ (i ^ nums[i-1])
        # final result is the integer which was missed in the given array from the 
    return result

nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))