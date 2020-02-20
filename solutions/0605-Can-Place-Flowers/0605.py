class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed or len(flowerbed) == 0:
            return False
        cnt = 0
        for plot in range(len(flowerbed)):  # range:0 - len(flowerbed)-1
            if flowerbed[plot] == 1:  # already planted flower
                continue
            if plot > 0 and flowerbed[plot-1] == 1:  # left planted flower
                continue
            if plot < len(flowerbed) - 1 and flowerbed[plot + 1] == 1:  # right planted flower
                continue
            flowerbed[plot] = 1
            cnt += 1
        if cnt >= n:
            return True
        else:
            return False

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    # flowerbed = [1,0,0,0,1,0,0]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))