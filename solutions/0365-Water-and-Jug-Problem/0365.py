class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # solution one: BFS
        from collections import deque
        queue = deque([[0, 0]])
        visited = set([(0, 0)])

        while queue:
            cur_x, cur_y = queue.pop()
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # x 加满水，y 加满水
                (x, cur_y), (cur_x, y),
                # x 清空水，y 清空水
                (0, cur_y), (cur_x, 0),
                # 把 x 壶的水灌进 y 壶，直至灌满或倒空
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # 把 X 壶的水灌进 Y 壶，直至灌满或倒空
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    queue.appendleft(item)  # 从队列左边加入元素
                    visited.add(item)
        return False

        # solution two: 裴蜀定理
        import math
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0