package br.edu.ufcg.coding_problems.crack_code.chapter4.question1;

import br.edu.ufcg.coding_problems.crack_code.chapter4.TreeNode;

public class BalancedTree extends TreeNode {

	public BalancedTree(Integer data) {
		super(data);
	}
	
	public boolean isBalanced(){
		int leftHeigh = this.getTreeHeight(this.left);
		int rightHeigh = this.getTreeHeight(this.right);
		
		return Math.abs(rightHeigh - leftHeigh) <= 1;
	}
}
