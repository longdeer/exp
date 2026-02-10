

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void inorder(struct TreeNode* node)
{
	if(node != NULL)
	{
		inorder(node->left);
		printf("node->val = %i\n", node->val);
		inorder(node->right);
	}
}


void preorder(struct TreeNode* node)
{
	if(node != NULL)
	{
		printf("node->val = %i\n", node->val);
		preorder(node->left);
		preorder(node->right);
	}
}


void postorder(struct TreeNode* node)
{
	if(node != NULL)
	{
		postorder(node->left);
		postorder(node->right);
		printf("node->val = %i\n", node->val);
	}
}

