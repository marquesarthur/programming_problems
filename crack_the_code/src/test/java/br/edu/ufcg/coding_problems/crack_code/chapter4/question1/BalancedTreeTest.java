package br.edu.ufcg.coding_problems.crack_code.chapter4.question1;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class BalancedTreeTest {

	private BalancedTree binaryTree;

	@Before
	public void setUp() {
		binaryTree = new BalancedTree(6);
	}

	@Test
	public void testIsBalancedForSingleNodeTree() {
		Assert.assertTrue(binaryTree.isBalanced());
	}

	@Test
	public void testIsBalancedForTreeWithOneLeftLeaf() {
		binaryTree.insert(5);
		Assert.assertTrue(binaryTree.isBalanced());
	}

	@Test
	public void testIsBalancedForTreeWithOneRightLeaf() {
		binaryTree.insert(8);
		Assert.assertTrue(binaryTree.isBalanced());
	}

	@Test
	public void testIsBalancedForNonBalancedTree() {
		binaryTree.insert(3);
		binaryTree.insert(2);

		Assert.assertFalse(binaryTree.isBalanced());
	}

	@Test
	public void testIsBalancedForBalancedTree() {
		binaryTree.insert(3);
		Assert.assertTrue(binaryTree.isBalanced());

		binaryTree.insert(9);
		Assert.assertTrue(binaryTree.isBalanced());

		binaryTree.insert(2);
		Assert.assertTrue(binaryTree.isBalanced());

		binaryTree.insert(4);
		Assert.assertTrue(binaryTree.isBalanced());

		binaryTree.insert(7);
		Assert.assertTrue(binaryTree.isBalanced());

		binaryTree.insert(10);
		Assert.assertTrue(binaryTree.isBalanced());
	}
}
