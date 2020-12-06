/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */


 // 将每两个相邻节点连接起来
 func connectTwoNode(node1 *Node, node2 *Node) {
	 if node1 == nil && node2 == nil {
		 return
	 }
	 node1.Next = node2

	 // 链接相同父节点的两个子节点
	 connectTwoNode(node1.Left, node1.Right)
	 connectTwoNode(node2.Left, node2.Right)
	 // 链接不同父节点的两个子节点
	 connectTwoNode(node1.Right, node2.Left)
 }

 func connect(root *Node) *Node {
	if root == nil {
		return nil
	}

	connectTwoNode(root.Left, root.Right)
	return root
}