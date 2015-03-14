package br.edu.ufcg.coding_problems.crack_code.chapter1.question4;

import java.util.ArrayList;
import java.util.List;

public class Anagram {

	private static final Character SPACE = new Character(' ');

	public static boolean isAnagram(String a, String b) {
		
		a = a.toLowerCase();
		b = b.toLowerCase();

		List<Character> charactersOfA = new ArrayList<Character>();

		for (int i = 0; i < a.length(); i++) {
			Character toBeInserted = new Character(a.charAt(i));
			if (!toBeInserted.equals(SPACE)) {
				charactersOfA.add(toBeInserted);
			}
		}

		for (int i = 0; i < b.length(); i++) {
			Character toBeRemoved = new Character(b.charAt(i));
			if (!toBeRemoved.equals(SPACE)) {
				if (charactersOfA.indexOf(toBeRemoved) == -1) {
					return false;
				} else {
					charactersOfA.remove(toBeRemoved);
				}
			}
		}
		return true;
	}

}
