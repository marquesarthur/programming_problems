package br.edu.ufcg.coding_problems.crack_code.chapter2.question4;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class SumLinkedLists {

	public static Node sum(Node a, Node b) {

		if (a == null && b == null) {
			throw new RuntimeException("Cannot sum null linked lists");
		}

		Node currentA = a;
		Node currentB = b;
		Node result = sumNodes(currentA, currentB);

		return result;
	}

	private static Node sumNodes(Node a, Node b) {

		int sum = 0;

		if (a != null) {
			sum += a.getValue();
			a = a.getNext();
		}

		if (b != null) {
			sum += b.getValue();
			b = b.getNext();
		}

		int valueToSum = sum % 10;

		boolean carryOver = sum > 9;

		Node result = new Node(valueToSum);

		sumNodes(result, a, b, carryOver);

		return result;
	}

	public static void sumNodes(Node result, Node a, Node b, boolean carryOver) {

		if (a == null && b == null) {
			return;
		}

		int sum = 0;

		if (a != null) {
			sum += a.getValue();
			a = a.getNext();
		}

		if (b != null) {
			sum += b.getValue();
			b = b.getNext();
		}

		int valueToSum = sum % 10;
		if (carryOver) {
			valueToSum += 1;
		}

		carryOver = sum > 9;

		if (result == null) {
			result = new Node(valueToSum);
		} else {
			result.append(valueToSum);
		}

		sumNodes(result, a, b, carryOver);
	}
}
