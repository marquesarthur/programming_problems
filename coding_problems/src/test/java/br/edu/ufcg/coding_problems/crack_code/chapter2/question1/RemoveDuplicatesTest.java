package br.edu.ufcg.coding_problems.crack_code.chapter2.question1;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class RemoveDuplicatesTest {

	private Node head;

	private Node expected;

	@Before
	public void setUp() {
		head = new Node(1);
		head.append(2);
		head.append(3);

		expected = new Node(1);
		expected.append(2);
		expected.append(3);
	}

	@Test(expected = RuntimeException.class)
	public void testRemoveDuplicatesFromNull() {
		RemoveDuplicates.removeDuplicates(null);
	}

	@Test
	public void testRemoveDuplicatesFromNonDuplicatedLinkedList() {
		Node nonDuplicated = RemoveDuplicates.removeDuplicates(head);
		
		System.out.println(nonDuplicated.toList());
		Assert.assertEquals(expected.toList(), nonDuplicated.toList());
	}

	@Test
	public void testRemoveDuplicatesFromDuplicatedLinkedList() {
		head.append(2);
		head.append(3);

		Node nonDuplicated = RemoveDuplicates.removeDuplicates(head);
		Assert.assertEquals(expected.toList(), nonDuplicated.toList());
	}
}
