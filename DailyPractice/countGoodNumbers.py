# import numpy as np
import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        modulus = 1000000007

        if n % 2 == 0:
            po = n // 2
            check = pow(5, po, modulus)
            # print("1", check)
            laterCheck = pow(4, po, modulus)
            # print("2", laterCheck)
            number = (laterCheck * check) % modulus
           
        else:
            enPr = n // 2 + 1
            oPr = n // 2
            number = (pow(5, enPr, modulus) * pow(4, oPr, modulus)) % modulus

        return number

solution = Solution()
answer = solution.countGoodNumbers(50)
print(answer)




