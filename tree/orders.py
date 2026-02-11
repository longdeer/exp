

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder(node :TreeNode):

	if  node:

		inorder(node.left)
		print(node.val)
		inorder(node.right)


def preorder(node :TreeNode):

	if  node:

		print(node.val)
		preorder(node.left)
		preorder(node.right)


def postorder(node :TreeNode):

	if  node:

		postorder(node.left)
		postorder(node.right)
		print(node.val)

