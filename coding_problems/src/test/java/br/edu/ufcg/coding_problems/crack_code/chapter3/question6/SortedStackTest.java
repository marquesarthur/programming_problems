package br.edu.ufcg.coding_problems.crack_code.chapter3.question6;


import java.util.Arrays;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class SortedStackTest {

	private SortedStack stack;

	@Before
	public void setUp() {
		this.stack = new SortedStack();
	}
	
	@Test
	public void testSortEmptyStack(){
		stack.sort();
	}
	
	@Test
	public void testSortSingleNodeStack(){
		stack.push(new Node(1));
		stack.sort();
		
		System.out.println(stack.toList());
		Assert.assertEquals(Arrays.asList(new Integer[]{1}), stack.toList());
	}
	
	@Test
	public void testSortNonOrderedStack(){
		stack.push(new Node(2));
		stack.push(new Node(1));
		stack.sort();
		
		System.out.println(stack.toList());
		Assert.assertEquals(Arrays.asList(new Integer[]{1, 2}), stack.toList());
	}
	
}
