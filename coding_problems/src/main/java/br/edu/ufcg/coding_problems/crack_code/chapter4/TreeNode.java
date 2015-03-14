package br.edu.ufcg.coding_problems.crack_code.chapter4;

import java.util.ArrayList;
import java.util.List;

public class TreeNode {

	public Integer data;

	public TreeNode left;

	public TreeNode right;

	public TreeNode(Integer data) {
		this.data = data;
		this.left = null;
		this.right = null;

	}

	public void insert(Integer data) {
		this.insert(this, data);
	}

	public void insert(TreeNode currentNode, Integer data) {
		if (currentNode.data > data) {
			if (currentNode.left != null) {
				this.insert(currentNode.left, data);
			} else {
				currentNode.left = new TreeNode(data);
			}
		} else {
			if (currentNode.right != null) {
				this.insert(currentNode.right, data);
			} else {
				currentNode.right = new TreeNode(data);
			}
		}
	}

	public TreeNode find(Integer data) {
		return find(this, data);
	}

	private TreeNode find(TreeNode currentNode, Integer data) {
		if (currentNode == null) {
			return null;
		} else if (currentNode.data == data) {
			return currentNode;
		} else if (currentNode.data > data) {
			return this.find(currentNode.left, data);
		} else {
			return this.find(currentNode.right, data);
		}
	}

	public List<Integer> preOrder() {
		List<Integer> result = new ArrayList<Integer>();
		this.traversePreOrder(this, result);
		return result;
	}

	public List<Integer> inOrder() {
		List<Integer> result = new ArrayList<Integer>();
		this.traverseInOrder(this, result);
		return result;
	}

	public List<Integer> postOrder() {
		List<Integer> result = new ArrayList<Integer>();
		this.traversePostOrder(this, result);
		return result;
	}

	private void traversePreOrder(TreeNode currentNode, List<Integer> result) {
		if (currentNode != null) {
			result.add(currentNode.data);
			this.traversePreOrder(currentNode.left, result);
			this.traversePreOrder(currentNode.right, result);
		}
	}

	private void traverseInOrder(TreeNode currentNode, List<Integer> result) {
		if (currentNode != null) {
			this.traverseInOrder(currentNode.left, result);
			result.add(currentNode.data);
			this.traverseInOrder(currentNode.right, result);
		}
	}

	private void traversePostOrder(TreeNode currentNode, List<Integer> result) {
		if (currentNode != null) {
			this.traversePostOrder(currentNode.left, result);
			this.traversePostOrder(currentNode.right, result);
			result.add(currentNode.data);
		}
	}

	public int getHeight() {
		return getTreeHeight(this);
	}

	public int getTreeHeight(TreeNode currentNode) {
		if (currentNode != null) {
			return 1 + Math.max(getTreeHeight(currentNode.left),
					getTreeHeight(currentNode.right));
		} else {
			return 0;
		}
	}
}
