from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for x in A:
            sum += x
        # 和不能被3整除，肯定不符合
        if sum % 3:
            return False
        
        left, right = 0, len(A)-1
        leftSum, rightSum = A[left], A[right]

        while left + 1 < right:
            # 左右都等于sum/3，中间肯定等于sum/3
            if leftSum == sum/3 and rightSum == sum/3:
                return True
            if leftSum != sum/3:
                left += 1
                leftSum += A[left]
            if rightSum != sum/3:
                right -= 1
                rightSum += A[right]
        return False

if __name__ == "__main__":
    A = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(Solution().canThreePartsEqualSum(A))