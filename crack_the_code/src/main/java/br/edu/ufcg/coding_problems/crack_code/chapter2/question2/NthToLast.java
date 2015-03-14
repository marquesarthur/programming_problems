package br.edu.ufcg.coding_problems.crack_code.chapter2.question2;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class NthToLast {

	public static Node find(int nth, Node head) {

		if (head == null) {
			throw new RuntimeException("Linked list cannot be null");
		}

		int linkedListSize = 0;
		Node current = head;

		while (current != null) {
			linkedListSize++;
			current = current.getNext();
		}

		int indexOfNth = linkedListSize - nth;

		if (indexOfNth < 1 || indexOfNth > linkedListSize) {
			throw new RuntimeException(
					"Bad request. The nth node cannot be lesser or greater than the linked list size");
		}

		current = head;
		int index = 0;
		while (current != null) {
			index++;
			if (index == indexOfNth) {
				return current;
			} else {
				current = current.getNext();
			}
		}

		return null;
	}
}
