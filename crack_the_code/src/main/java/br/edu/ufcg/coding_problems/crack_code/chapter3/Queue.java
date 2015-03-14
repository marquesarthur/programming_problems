package br.edu.ufcg.coding_problems.crack_code.chapter3;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class Queue {

	private Node first;

	private Node last;

	public Queue() {
		first = null;
		last = null;
	}

	public void enqueue(Node node) {
		if (first == null) {
			first = node;
			last = node;
		} else {
			last.setNext(node);
			last = last.getNext();
		}
	}

	public Node dequeue() {
		if (first != null) {
			Node result = new Node(first.getValue());
			first = first.getNext();
			return result;
		}
		return null;
	}
}
