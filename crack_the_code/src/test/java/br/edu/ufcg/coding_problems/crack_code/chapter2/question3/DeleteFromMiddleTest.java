package br.edu.ufcg.coding_problems.crack_code.chapter2.question3;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class DeleteFromMiddleTest {

	private Node head;
	
	private Node expected;

	@Before
	public void setUp() {
		head = new Node(1);
		head.append(2);
		head.append(3);
		head.append(4);
		head.append(5);
		
		expected = new Node(1);
		expected.append(2);
		expected.append(4);
		expected.append(5);
	}
	
	@Test
	public void testDeleteFromMiddle(){
		System.out.println(head.toList());
		Node current = head;
		while (current.getValue() != 3){
			current = current.getNext();
		}
		
		DeleteFromMiddle.delete(current);
		
		System.out.println(head.toList());
		
		Assert.assertEquals(expected.toList(), head.toList());
		
		
		
	}
	
}
