package br.edu.ufcg.coding_problems.crack_code.chapter8.question4;

import java.util.ArrayList;
import java.util.List;

public class StringPermutation {

	public static List<String> getPermutations(String string) {

		List<String> permutations = new ArrayList<String>();
		if (string == null) {
			throw new RuntimeException("Cannot permute null string");
		}
		if (string.length() == 0) {
			permutations.add("");
			return permutations;
		}

		String currentCharacter = string.substring(0, 1);
		String remainder = string.substring(1, string.length());

		List<String> words = getPermutations(remainder);
		for (String s : words) {
			for (int i = 0; i <= s.length(); i++) {
				StringBuffer str = new StringBuffer();
				str.append(s.substring(0, i));
				str.append(currentCharacter);
				str.append(s.substring(i, s.length()));
				permutations.add(str.toString().trim());
			}
		}

		return permutations;
	}

}
