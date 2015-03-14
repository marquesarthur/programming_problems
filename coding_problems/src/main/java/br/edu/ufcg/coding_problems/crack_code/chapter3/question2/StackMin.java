package br.edu.ufcg.coding_problems.crack_code.chapter3.question2;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;
import br.edu.ufcg.coding_problems.crack_code.chapter3.Stack;

public class StackMin {

	private Stack head;

	private Stack minHead;

	public StackMin() {
		this.head = null;
	}

	public void push(Node node) {
		head.push(node);
		if (minHead.peek().getValue() > node.getValue()) {
			minHead.push(node);
		}
	}

	public Node pop() {

		Node result = head.pop();

		if (minHead.peek().getValue() == result.getValue()) {
			minHead.pop();
		}

		return result;
	}
}
