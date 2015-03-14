package br.edu.ufcg.coding_problems.crack_code.chapter3.question5;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class MyQueueTest {

	private MyQueue myqueue;

	@Before
	public void setUp() {
		this.myqueue = new MyQueue();
	}

	@Test
	public void testPush() {
		Node n = new Node(1);
		myqueue.push(n);
	}

	@Test
	public void testPushPushPop() {
		Node n = new Node(1);
		myqueue.push(n);
		n = new Node(2);
		myqueue.push(n);

		n = myqueue.pop();

		Assert.assertEquals(1, n.getValue());
	}

	@Test
	public void testPushPushPopPushPop() {
		Node n = new Node(1);
		myqueue.push(n);
		n = new Node(2);
		myqueue.push(n);

		n = myqueue.pop();

		Assert.assertEquals(1, n.getValue());

		n = new Node(3);
		myqueue.push(n);

		n = myqueue.pop();

		Assert.assertEquals(2, n.getValue());
	}
}
