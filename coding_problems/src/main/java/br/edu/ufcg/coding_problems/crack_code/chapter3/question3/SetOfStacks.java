package br.edu.ufcg.coding_problems.crack_code.chapter3.question3;

import java.util.ArrayList;
import java.util.List;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;
import br.edu.ufcg.coding_problems.crack_code.chapter3.Stack;

public class SetOfStacks {

	private List<SizedStack> setOfStacks;

	private int threshold;

	public SetOfStacks(int threshold) {
		this.setOfStacks = new ArrayList<SetOfStacks.SizedStack>();
		this.threshold = threshold;
	}

	public void push(Node node) {
		if (setOfStacks.isEmpty()) {
			SizedStack stack = new SizedStack();
			stack.push(node);
			setOfStacks.add(stack);
		} else {
			SizedStack currentStack = setOfStacks.get(setOfStacks.size() - 1);

			if (currentStack.getSize() < this.threshold) {
				setOfStacks.get(setOfStacks.size() - 1).push(node);
			} else {
				SizedStack stack = new SizedStack();
				stack.push(node);
				setOfStacks.add(stack);
			}
		}
	}

	public Node pop() {
		if (setOfStacks.isEmpty()) {
			return null;
		}

		SizedStack currentStack = setOfStacks.get(setOfStacks.size() - 1);
		Node result = currentStack.pop();
		if (currentStack.isEmpty()) {
			setOfStacks.remove(setOfStacks.size() - 1);
		}

		return result;
	}

	public class SizedStack extends Stack {

		private int size = 0;

		@Override
		public void push(Node node) {
			super.push(node);
			size++;
		}

		@Override
		public Node pop() {
			if (size > 0) {
				size--;
			}
			return super.pop();
		}

		public int getSize() {
			return size;
		}
	}
}
