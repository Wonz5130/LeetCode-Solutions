from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # solution one: sliding window
        i, j = 1, 1
        sum = 0
        res = []

        while i <= target // 2:
            if sum < target:
                # j + 1
                sum += j
                j += 1
            elif sum > target:
                # i + 1
                sum -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)
                # i + 1
                sum -= i
                i += 1

        return res

        # solution two: formula
        res = []
        
        for y in range(1, target // 2 + 2):  # range:[ )
            x = (1/4 + y**2 + y - 2*target) ** (1/2) + 0.5
            if type(x) != complex and x - int(x) == 0:  # x can't be complex and x must be int
                res.append(list(range(int(x), y + 1)))
        
        return res

        # solution three
        i, res = 1, []

        while i*(i+1)/2 < target:
            if not (target - i*(i+1)/2) % (i+1):
                x = int((target - i*(i+1)/2) // (i+1))
                res.append(list(range(x, x+i+1)))
            i += 1
        
        # reverse
        return res[::-1]

if __name__ == "__main__":
    target = 9
    print(Solution().findContinuousSequence(target))  