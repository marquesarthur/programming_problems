package br.edu.ufcg.el_dorado;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

class ABX_Problem {

	public static void main(String[] args) throws java.lang.Exception {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(
					System.in));
			String input = br.readLine();

			PrettyPrintABX abx = new PrettyPrintABX(input);
			System.out.print(abx.toString());

		} catch (Exception ex) {
			System.out.println(0);
		}
	}

	/**
	 * Class to pretty print numbers. Given 3 numbers(positive integers) A, B
	 * and X, it prints the numbers from 1 to X. But for multiples of A print
	 * "A" instead of the number and for the multiples of B print "B". For
	 * numbers which are multiples of both A and B print "AB".
	 */
	static class PrettyPrintABX {
		
		private static final String WHITE_SPACE = " ";

		private static final int INDEX_OF_A = 0;

		private static final int INDEX_OF_B = 1;

		private static final int INDEX_OF_X = 2;

		private static final String B = "B";

		private static final String A = "A";

		private static final String AB = "AB";

		private int a;

		private int b;

		private int x;

		public PrettyPrintABX(String input) {
			String[] inputNumbers = input.split(WHITE_SPACE);
			this.a = Integer.parseInt(inputNumbers[INDEX_OF_A]);
			this.b = Integer.parseInt(inputNumbers[INDEX_OF_B]);
			this.x = Integer.parseInt(inputNumbers[INDEX_OF_X]);
		}

		public String toString() {
			List<String> output = new ArrayList<String>();
			for (int i = 1; i <= x; i++) {
				addFormatedNumber(output, i);
			}
			String result = removeBracketsAndCommas(output);
			return result;
		}

		private String removeBracketsAndCommas(List<String> output) {
			return output.toString().replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(",", "");
		}

		private void addFormatedNumber(List<String> output, int currentNumber) {
			boolean multipleOfA = isMultipleOf(currentNumber, a);
			boolean multipleOfB = isMultipleOf(currentNumber, b);

			if (multipleOfA && multipleOfB) {
				output.add(AB);
			} else if (multipleOfA) {
				output.add(A);
			} else if (multipleOfB) {
				output.add(B);
			} else {
				output.add(String.valueOf(currentNumber));
			}
		}

		private boolean isMultipleOf(int number, int multiple) {
			return number % multiple == 0;
		}
	}
}
