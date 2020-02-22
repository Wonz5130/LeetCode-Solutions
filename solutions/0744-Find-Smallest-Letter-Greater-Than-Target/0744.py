class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low, high = 0, len(letters) - 1
        while low <= high:
            mid = int((low + high) / 2)  # element in list must be int
            if letters[mid] <= target:
                low = mid + 1
            else:
                if mid < 1 or (mid >= 1 and letters[mid-1] <= target):
                    return letters[mid]
                high = mid - 1
        return letters[0]  # 'z' < 'a'

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    print(Solution().nextGreatestLetter(letters, target))