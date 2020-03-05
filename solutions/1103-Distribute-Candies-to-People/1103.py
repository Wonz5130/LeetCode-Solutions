from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        step = 0
        while candies > 0:
            res[step % num_people] += min(candies, step + 1)
            step += 1  # next person
            candies -= step  # the remaining candies
        return res

if __name__ == "__main__":
    candies = 7
    num_people = 4
    print(Solution().distributeCandies(candies, num_people))