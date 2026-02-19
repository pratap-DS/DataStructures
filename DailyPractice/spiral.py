
from ast import List
import math
def spiralOrder(matrix):
    
    m = len(matrix)
    n = len(matrix[0])

    total = m*n
    
    counter = min(m,n)
    counter = math.ceil(counter/2)
    count = 1
    
    top = n            
    right = m -1
    bottom = n - 1
    left = m - 2
    
    arr = []
    r = 0
    c = 0
    
    while (count <= counter):
        
        if m>1:
            for i in range(c,top):
                print("top",r,i)
                arr.append(matrix[r][i])
                # count += 1

                
            c = i
            top -= 1
                
            for j in range(r+1,right+1):
                print("right",j,c)
                arr.append(matrix[j][c])
                # count += 1
                
                r = j
            right -= 1
            
            if bottom >= 1:
                for k in range(c-1,c-bottom-1, -1):
                    # count += 1

                    print(r,k)
                    arr.append(matrix[r][k])
                    # count += 1
            
                c = k
            bottom -= 2
            # print("bottom", bottom)
            for l in range(r-1, r-left-1, -1):
                # count += 1
                print("left",l,c)
                arr.append(matrix[l][c])

                r = l

            left -= 2
            c += 1
            count += 1

        else:
            arr.extend(matrix[0])
            return arr

        # print(count)
        
    return arr

matrix = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7] 
matrix = [[6,9,7]]

matrix = [[1,2],[3,4]]

print(spiralOrder(matrix))


import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        total = m*n

        counter = min(m,n)
        counter = math.ceil(counter/2)
        count = 0

        top = n            
        right = m -1
        bottom = n - 1
        left = m - 2

        arr = []
        r = 0
        c = 0

        while (count <= total):

            if m>1:
                
                if count >= m*n:
                    return arr
            
                for i in range(c,top):
                    arr.append(matrix[r][i])
                    count += 1
                c = i
                top -= 1
                
                if count >= m*n:
                    return arr

                for j in range(r+1,right+1):
                    arr.append(matrix[j][c])
                    count += 1

                r = j
                right -= 1
                
                if count >= m*n:
                    return arr

                if bottom >= 1:
                    for k in range(c-1,c-bottom-1, -1):
                        count += 1
                        arr.append(matrix[r][k])
                    c = k
                bottom -= 2
                
                if count >= m*n:
                    return arr
                for l in range(r-1, r-left-1, -1):
                    count += 1
                    arr.append(matrix[l][c])
                r = l

                left -= 2
                c += 1
                
            else:
                arr.extend(matrix[0])
                return arr

        return arr

                
            
            
            
            
            
            

            
            
            
            
        