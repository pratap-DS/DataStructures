"""
Count Sort Algorithm with Negative Numbers
-------------------------------------------
This implementation sorts an array using the Count Sort algorithm and handles negative numbers by offsetting indices.

Steps:
1. **Handle Empty Input:**
   - If the input array is empty, return an empty list immediately to avoid errors with min() or max().
   Example:
   Input: []
   Output: []

2. **Find the Range of Input:**
   - Determine the smallest (`minn`) and largest (`maxx`) values in the array.
   - Calculate the range: `rnge = (maxx - minn) + 1`.
   - Use `offset = -minn` to shift the numbers so the smallest value (`minn`) maps to index `0`.
   Example:
   Input: [-5, -10, 0, -3, 8, 5, -1, 10]
   Computed Values: `minn = -10`, `maxx = 10`, `rnge = 21`, `offset = 10`.

3. **Create and Populate the Count Array:**
   - Create a `countArray` of size `rnge`, initialized to 0.
   - For each number in the input array, increment the count at its corresponding index:
     `index = num + offset`.
   Example:
   Input: [-5, -10, 0, -3, 8, 5, -1, 10]
   Count Array: [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

4. **Reconstruct the Sorted Array:**
   - Create an empty list `final` to store the sorted elements.
   - Iterate through the `countArray`. For each index with a count greater than 0:
     - Append the value `(index - offset)` to the list, repeated `countArray[index]` times.
   Example:
   Count Array: [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

    Initialize an empty list final to store the sorted numbers.
    Iterate over the countArray:
    For each index j with a count greater than zero, append the corresponding value (j - offset) to the final list, repeated countArray[j] times.
    The subtraction of offset converts the adjusted index back to the original number.
    Example: For the count array: [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

    Index 0: 0 - 10 = -10, count = 1 → Add [-10]
    Index 5: 5 - 10 = -5, count = 1 → Add [-5]
    Index 7: 7 - 10 = -3, count = 1 → Add [-3]
    Index 9: 9 - 10 = -1, count = 1 → Add [-1]
    Index 10: 10 - 10 = 0, count = 1 → Add [0]
    Index 15: 15 - 10 = 5, count = 1 → Add [5]
    Index 18: 18 - 10 = 8, count = 1 → Add [8]
    Index 20: 20 - 10 = 10, count = 1 → Add [10]
    Final sorted array: [-10, -5, -3, -1, 0, 5, 8, 10]

   Sorted Array: [-10, -5, -3, -1, 0, 5, 8, 10]

5. **Return the Sorted Array:**
   - Return the reconstructed `final` list.

Time Complexity:
- Finding `min()` and `max()`: O(n)
- Filling the count array: O(n)
- Reconstructing the sorted array: O(rnge)
- Overall: O(n + rnge)

Space Complexity:
- Count Array: O(rnge)
- Final List: O(n)
- Overall: O(n + rnge)

Example:
Input: [-5, -10, 0, -3, 8, 5, -1, 10]
Output: [-10, -5, -3, -1, 0, 5, 8, 10]
"""


#  key points are, 
    # finding range
    # defining offset
    # creating count array from original array
    # creating final sorted array from count array(the logic is little tricky)


def countSort(ar):

    minn = min(ar)
    maxx = max(ar)
    rnge = (maxx-minn)+1
    offset = -minn

    countArray = [0]*rnge

    for i in ar:
        countArray[i+offset] += 1
    print(countArray)
    final = []
    for j in range(len(countArray)):
        final.extend([j-offset]*countArray[j])

    return final

a = [9,4,2,7,8,10,1,8,0,-5,-1,-3]
f = countSort(a)
print(f)






