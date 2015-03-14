package br.edu.ufcg.coding_problems.crack_code.chapter1.question3;

public class RemoveDuplicatedCharacters {

	public static String removeDuplicates(String in) {

		if (in == null) {
			throw new RuntimeException(
					"String is null. Cannot remove duplicates");
		}
		if (in.isEmpty()) {
			return in;
		}

		int current = 0;
		while (current < in.length()) {
			String actual = in.substring(current, current + 1);
			String head = in.substring(0, current + 1);
			in = head + in.substring(current + 1).replaceAll(actual, "");
			current++;
		}

		System.out.println(in);

		return in;
	}

}