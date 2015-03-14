package br.edu.ufcg.coding_problems.crack_code.chapter4.question2;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter4.TreeNode;

@RunWith(JUnit4.class)
public class ArrayToTreeTest {

	@Test(expected=RuntimeException.class)
	public void testArrayToTreeForNullArray(){
		ArrayToTree.getTree(null);
	}
	
	@Test(expected=RuntimeException.class)
	public void testArrayToTreeForEmptyArray(){
		ArrayToTree.getTree(new Integer[]{});
	}
	
	@Test
	public void testArrayToTreeForSingleElementArray(){
		TreeNode tree = ArrayToTree.getTree(new Integer[]{1});
		int height = tree.getHeight();
		
		Assert.assertEquals(1, height);
	}
	
	@Test
	public void testArrayToTreeForArray(){
		TreeNode tree = ArrayToTree.getTree(new Integer[]{2, 3, 4, 6, 7, 9 , 10});
		int height = tree.getHeight();
		
		Assert.assertEquals(3, height);
	}
}
