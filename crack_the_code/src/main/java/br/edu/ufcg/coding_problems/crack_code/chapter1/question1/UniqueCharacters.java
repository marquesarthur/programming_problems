package br.edu.ufcg.coding_problems.crack_code.chapter1.question1;

import java.util.ArrayList;
import java.util.List;

public class UniqueCharacters {

	public static boolean isUnique(String string) {
		if (string == null) {
			throw new RuntimeException("Cannot validate null string");
		}
		if (string.isEmpty()) {
			return true;
		}

		List<Character> charactersOfString = new ArrayList<Character>();

		for (char c : string.toCharArray()) {
			if (charactersOfString.contains(new Character(c))) {
				return false;
			}
			charactersOfString.add(new Character(c));
		}

		return true;
	}
}
