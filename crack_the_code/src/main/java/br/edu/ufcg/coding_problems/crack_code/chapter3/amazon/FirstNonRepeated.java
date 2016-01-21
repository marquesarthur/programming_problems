package br.edu.ufcg.coding_problems.crack_code.chapter3.amazon;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class FirstNonRepeated {

	private Queue<Character> LastNonRepeated;

	private Map<Character, Integer> mapCharacterCount;

	public FirstNonRepeated() {
		this.LastNonRepeated = new LinkedList<Character>();
		mapCharacterCount = new HashMap<Character, Integer>();
	}

	public void push(Character c) {

		if (!mapCharacterCount.containsKey(c)) {
			mapCharacterCount.put(c, 0);
		}
		Integer count = mapCharacterCount.get(c);
		count++;

		if (count > 1) {
			if (getlastNonRepeated() != null) {
				if (getlastNonRepeated().equals(c)) {
					this.LastNonRepeated.poll();
				}
			}
		} else {
			this.LastNonRepeated.add(c);
		}
		mapCharacterCount.put(c, count);
	}

	public Character getlastNonRepeated() {
		return this.LastNonRepeated.peek();
	}

}
