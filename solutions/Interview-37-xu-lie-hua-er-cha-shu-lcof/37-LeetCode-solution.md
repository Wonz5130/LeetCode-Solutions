> LeetCode 剑指 Offer 37. 序列化二叉树【Hard】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

请实现两个函数，分别用来序列化和反序列化二叉树。

**示例:** 

    你可以将以下二叉树：
    	1
       / \
      2   3
         / \
        4   5
    
    序列化为 "[1,2,3,null,null,4,5]"

注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

## 思路

**BFS**

## 代码

### Python3

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        import collections
        if not root:
            return "[]"
        
        queue = collections.deque()
        queue.append(root)
        res = []
        # 层序遍历BFS
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import collections
        if data == "[]":
            return
        
        # 去掉首尾括号，根据逗号进行切片
        vals, i = data[1:-1].split(","), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            # 构建左子树
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            # 构建右子树
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-37-xu-lie-hua-er-cha-shu-lcof)

[面试题37. 序列化二叉树（层序遍历 BFS ，清晰图解）](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/)