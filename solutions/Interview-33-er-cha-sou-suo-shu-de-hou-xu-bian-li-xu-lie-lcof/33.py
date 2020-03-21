from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            # 根节点小于等于1个
            if i >= j:
                return True
            l = i
            # 左子树
            while postorder[l] < postorder[j]:
                l += 1
            # 找到第一个大于根节点的节点，记为 m
            m = l
            # 右子树
            while postorder[l] > postorder[j]:
                l += 1
            # postorder[j]是根
            return l == j and recur(i, m - 1) and recur(m, j - 1)
        
        return recur(0, len(postorder) - 1)