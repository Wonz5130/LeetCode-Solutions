class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # solution one: binary search
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return int(mid)

        # # solution two: Newton's method
        # res = x
        # while res * res > x:
        #     res = (res + x / res) / 2
        # return int(res)

        # # solution three: math
        # import math
        # return int(math.sqrt(x))

if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))