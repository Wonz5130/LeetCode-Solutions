from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j]:
                        if rating[j] < rating[k]:
                            count += 1
                    elif rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            count += 1
        return count

if __name__ == "__main__":
    rating = [2,5,3,4,1]
    print(Solution().numTeams(rating))