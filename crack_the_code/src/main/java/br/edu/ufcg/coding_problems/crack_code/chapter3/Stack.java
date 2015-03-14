package br.edu.ufcg.coding_problems.crack_code.chapter3;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class Stack {

	protected Node head;

	public Stack() {
		this.head = null;
	}

	public void push(Node node) {
		if (head == null) {
			head = node;
		} else {
			node.setNext(head);
			head = node;
		}
	}

	public Node pop() {
		if (head == null) {
			return null;
		}

		Node result = new Node(head.getValue());
		this.head = head.getNext();

		return result;
	}

	public Node peek() {
		return head;
	}
	
	public boolean isEmpty(){
		return head == null;
	}
	
	
}
