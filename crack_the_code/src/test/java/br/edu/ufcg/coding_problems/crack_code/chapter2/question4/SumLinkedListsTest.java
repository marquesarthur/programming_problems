package br.edu.ufcg.coding_problems.crack_code.chapter2.question4;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

@RunWith(JUnit4.class)
public class SumLinkedListsTest {

	private Node a;

	private Node b;

	private Node result;

	@Test(expected = RuntimeException.class)
	public void testSumWithNullLists() {
		SumLinkedLists.sum(null, null);
	}

	@Test
	public void testSumWithEqualSizeLists() {
		a = new Node(3);
		a.append(1);
		a.append(5);

		b = new Node(5);
		b.append(9);
		b.append(2);

		result = new Node(8);
		result.append(0);
		result.append(8);

		Node sum = SumLinkedLists.sum(a, b);
		Assert.assertEquals(result.toList(), sum.toList());
	}

	@Test
	public void testSumOfNullBList() {
		a = new Node(3);
		a.append(1);
		a.append(5);

		result = new Node(3);
		result.append(1);
		result.append(5);

		Node sum = SumLinkedLists.sum(a, null);
		Assert.assertEquals(result.toList(), sum.toList());
	}

	@Test
	public void testSumOfNullAList() {
		b = new Node(5);
		b.append(9);
		b.append(2);

		result = new Node(5);
		result.append(9);
		result.append(2);

		Node sum = SumLinkedLists.sum(null, b);
		Assert.assertEquals(result.toList(), sum.toList());
	}

}
