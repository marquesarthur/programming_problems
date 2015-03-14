package br.edu.ufcg.coding_problems.crack_code.chapter3.question1;

public class ArrayWithThreeStacks {

	private Integer[] stacks;
	int currentA;
	int currentB;
	int currentC;

	public ArrayWithThreeStacks(int size) {
		this.stacks = new Integer[size];
		this.currentA = 0;
		this.currentB = 1;
		this.currentC = 2;
	}

	public void push(int stackNumber, int value) {
		switch (stackNumber) {
		case 1:
			pushIntoStack(0, value, stackNumber);
			break;
		case 2:
			pushIntoStack(1, value, stackNumber);
			break;
		case 3:
			pushIntoStack(2, value, stackNumber);
			break;
		default:
			throw new RuntimeException(
					"Array contain only 3 stacks: [1, 2, or 3]");
		}
	}

	private void pushIntoStack(int carry, int value, int stackNumber) {
		int index = (currentA * 3) + carry;

		if (index >= stacks.length) {
			throw new RuntimeException(String.format(
					"Cannot push into stack %n. Stack is full", stackNumber));
		}

		if (stacks[index] != null) {
			index = (currentA * 3) + carry;
		}
		stacks[index] = new Integer(value);
	}

	public Integer pop(int stackNumber) {
		Integer result = null;
		switch (stackNumber) {
		case 1:
			result = stacks[currentA];
			stacks[currentA] = null;
			if (currentA != 0) {
				currentA -= 3;
			}
			break;
		case 2:
			result = stacks[currentB];
			stacks[currentB] = null;
			if (currentB != 1) {
				currentB -= 3;
			}
			break;
		case 3:
			result = stacks[currentC];
			stacks[currentC] = null;
			if (currentC != 2) {
				currentC -= 3;
			}
			break;
		default:
			throw new RuntimeException(
					"Array contain only 3 stacks: [1, 2, or 3]");
		}
		return result;
	}

}
