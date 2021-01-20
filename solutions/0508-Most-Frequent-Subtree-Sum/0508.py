# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        import collections
        res_dic = collections.defaultdict(int)
        # 计算子树元素和
        def dfs(node):
            # 递归边界
            if not node:
                return 0
            tmp_sum = dfs(node.left) + node.val + dfs(node.right)
            res_dic[tmp_sum] += 1
            return tmp_sum
        
        if not root:
            return []
        dfs(root)
        max_cnt = 0
        for cnt in res_dic.values():
            max_cnt = max(max_cnt, cnt)
        return [key for key, cnt in res_dic.items() if cnt == max_cnt]