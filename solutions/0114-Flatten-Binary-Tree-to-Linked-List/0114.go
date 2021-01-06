/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	// 递归调用
	flatten(root.Left)
	flatten(root.Right)

	// 后序遍历：左-右-根
	// 左右子树拉平成链表
	var left = new(TreeNode)
	left = root.Left
	var right = new(TreeNode)
	right = root.Right

	// 左子树作为右子树
	root.Left = nil
	root.Right = left

	// 原先右子树接到当前右子树末端
	var p = new(TreeNode)
	p = root
	// 找到当前右子树末端
	for {
		if p.Right == nil {
			break
		}
		p = p.Right
	} 
	p.Right = right
}