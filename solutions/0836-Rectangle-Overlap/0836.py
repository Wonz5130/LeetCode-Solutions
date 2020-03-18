class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 左小角取 max
        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])
        # 右上角取 min
        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])
       
       # 判断是否重叠
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False