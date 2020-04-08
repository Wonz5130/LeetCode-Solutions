import collections

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        q = collections.deque()
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            if (x, y) not in visited and self.sum_rc(x, y) <= k:
                visited.add((x, y))
                for dx, dy in [(1, 0), (0, 1)]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        q.append((x + dx, y + dy))
        return len(visited)
    
    # 计算数位和
    def sum_rc(self, row, col):
        temp = 0
        while row > 0:
            temp += row % 10
            row //= 10
        while col > 0:
            temp += col % 10
            col //= 10
        return temp