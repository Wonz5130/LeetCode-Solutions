class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # solution one：模拟
        n = len(moves)
        left, right, up, down = 0, 0, 0, 0
        for i in range(n):
            if moves[i] == 'L':
                left += 1
            elif moves[i] == 'R':
                right += 1
            elif moves[i] == 'U':
                up += 1
            else:
                down += 1
        if left == right and up == down:
            return True
        else:
            return False
        
        # solution two：数学
        import collections
        c = Counter(moves)
        return c["U"] == c["D"] and c["L"] == c["R"]

        # solution three：数学
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")