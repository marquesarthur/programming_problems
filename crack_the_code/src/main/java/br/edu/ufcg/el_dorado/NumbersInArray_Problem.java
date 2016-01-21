package br.edu.ufcg.el_dorado;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

class NumbersInArray_Problem {

	public static void main(String[] args) throws java.lang.Exception {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(
					System.in));
			String input = br.readLine();

			// construct the array of numbers based on N and M
			ArrayOfNumbers array = new ArrayOfNumbers(input);

			// read the array
			input = br.readLine();
			array.readArray(input);

			for (String line = null; (line = br.readLine()) != null;) {
				System.out.println(array.contains(Integer.valueOf(line)));
			}

		} catch (Exception ex) {
			System.out.println(0);
		}
	}

	/**
	 * Array of numbers. Takes input of integers N and M, followed by N more
	 * integers and then M more integers. For each of the last M numbers, the
	 * program outputs true, if that number was present in the array of N
	 * numbers, output False otherwise.
	 */
	static class ArrayOfNumbers {

		private static final String WHITE_SPACE = " ";

		private static final int INDEX_OF_N = 0;

		private static final int INDEX_OF_M = 1;

		private static final int MAX_N = 20000;

		private static final int MAX_M = 15000;

		private static final int MIN = 0;

		private int n;

		private int m;

		// para essa questao, nao ha diferenca em checar o contains com um
		// inteiro ou um string,
		// porem segui o enunciado e tratei como um array de inteiros
		private List<Integer> numbers;

		public ArrayOfNumbers(String input) {
			String[] inputNumbers = input.split(WHITE_SPACE);
			this.n = parseInput(inputNumbers, INDEX_OF_N, MAX_N, MIN, "N");
			this.m = parseInput(inputNumbers, INDEX_OF_M, MAX_M, MIN, "M");
			this.numbers = new ArrayList<Integer>();
		}

		private int parseInput(String[] inputNumbers, int index, int max,
				int min, String field) {
			int value = Integer.parseInt(inputNumbers[index]);
			if (value < min || value >= max) {
				throw new RuntimeException(
						String.format("Constraint violation, %s - %s > %s",
								field, value, max));
			}
			return value;
		}

		public void readArray(String input) {
			for (String number : input.split(WHITE_SPACE)) {
				numbers.add(Integer.parseInt(number));
			}
		}

		public String contains(Integer number) {
			if (numbers.contains(number)) {
				return "True";
			} else {
				return "False";
			}
		}
	}
}
