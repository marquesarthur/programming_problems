package br.edu.ufcg.coding_problems.crack_code.chapter3.question6;

import java.util.ArrayList;
import java.util.List;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;
import br.edu.ufcg.coding_problems.crack_code.chapter3.Stack;

public class SortedStack extends Stack {

	public void sort() {
		Stack aux = new Stack();

		while (!this.isEmpty()) {
			Node topOfStack = this.pop();

			while (!aux.isEmpty()
					&& aux.peek().getValue() < topOfStack.getValue()) {
				this.push(aux.pop());

			}
			aux.push(topOfStack);
		}
		this.head = aux.peek();

	}

	public List<Integer> toList() {
		List<Integer> result = new ArrayList<Integer>();

		Node current = this.head;

		while (current != null) {
			result.add(new Integer(current.getValue()));
			current = current.getNext();
		}
		return result;
	}
}
