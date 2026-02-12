

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


var inorder = function(node) {

	if(node) {

		inorder(node.left);
		console.log(node.val);
		inorder(node.right)
	}
}


var preorder = function(node) {

	if(node) {

		console.log(node.val);
		preorder(node.left);
		preorder(node.right)
	}
}


var postorder = function(node) {

	if(node) {

		postorder(node.left);
		postorder(node.right);
		console.log(node.val)
	}
}

