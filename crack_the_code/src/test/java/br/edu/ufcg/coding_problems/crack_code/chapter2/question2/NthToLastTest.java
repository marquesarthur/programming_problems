package br.edu.ufcg.coding_problems.crack_code.chapter2.question2;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class NthToLastTest {

	private Node head;

	@Before
	public void setUp() {
		head = new Node(1);
		head.append(2);
		head.append(3);
		head.append(4);
		head.append(5);
		head.append(6);
		head.append(7);
	}

	@Test(expected = RuntimeException.class)
	public void testFindNthOfNullLinkedList() {
		NthToLast.find(1, null);
	}

	@Test
	public void testFindNthOfSingleNodeLinkedList() {
		head = new Node(1);
		Node node = NthToLast.find(0, head);
		Assert.assertEquals(node.getValue(), head.getValue());
	}

	@Test
	public void testFindNthOfLinkedList() {
		Node node = NthToLast.find(2, head);
		Assert.assertEquals(5, node.getValue());
	}

	@Test(expected = RuntimeException.class)
	public void testFindNthOfLinkedListWithNegativeNth() {
		NthToLast.find(-2, head);
	}

	@Test(expected = RuntimeException.class)
	public void testFindNthOfLinkedListWithNthGreaterThanListSize() {
		NthToLast.find(8, head);
	}
}
