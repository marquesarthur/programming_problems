package br.edu.ufcg.el_dorado;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class ClosestToFibonacci {
	
	public static void main(String[] args) throws java.lang.Exception {
		try {
			Fibonacci fibonacci = Fibonacci.getInstance();
			BufferedReader br = new BufferedReader(new InputStreamReader(
					System.in));
			Integer n = Integer.parseInt(br.readLine());
			for (String line = null; (line = br.readLine()) != null;) {
				if (line.isEmpty()){
					break;
				}
				Long number = Long.parseLong(line);
				System.out.println(fibonacci
						.getNextFibonacciGreaterThan(number));
			}
		} catch (Exception ex) {
			ex.printStackTrace();
			System.out.println(0);
		}
	}

	/**
	 * Class to compute Fibonacci numbers. It stores previously computed numbers
	 * in a map in order to speed the processing time. The computed numbers are
	 * also stored in list, thus it will be possible to find the next fibonacci
	 * number greater than a given number.
	 * 
	 * Class is a singleton. hence, it will assure that all its previously
	 * computed numbers will share the same instance and no re-processing is
	 * done
	 */
	static class Fibonacci {

		private static Fibonacci instance;

		private Map<Integer, Long> fibonnaciSequenceMap;

		private List<Long> fibonacciNumbers;

		public Fibonacci() {
			this.fibonnaciSequenceMap = new HashMap<Integer, Long>();
			this.fibonacciNumbers = new ArrayList<Long>();
			computeFibonacciUntil(60);
		}

		private void computeFibonacciUntil(int n) {
			for (int i = 2; i <= n; i++) {
				fibonnaci(i);
			}
		}

		/**
		 * Gets the first fibonacci number greater than n. Method relies on the
		 * fibonacci numbers stored in the {@code fibonacciNumbers} list
		 * 
		 * @param n
		 *            Input number
		 * @return first fibonacci number greater than n
		 */
		public Long getNextFibonacciGreaterThan(Long n) {
			List<Long> values = new ArrayList<Long>();
			values.addAll(fibonacciNumbers);
			Collections.sort(values);

			Collections.sort(values);
			for (Long currentFibonnaci : values) {
				if (currentFibonnaci > n) {
					return currentFibonnaci;
				}
			}
			return null;
		}

		public Long fibonnaci(int n) {
			if (fibonnaciSequenceMap.containsKey(n)) {
				return fibonnaciSequenceMap.get(n);
			} else if (n == 0) {
				fibonnaciSequenceMap.put(n, new Long(1));
				fibonacciNumbers.add(new Long(1));
				return new Long(1);
			} else if (n == 1) {
				fibonnaciSequenceMap.put(n, new Long(1));
				fibonacciNumbers.add(new Long(1));
				return new Long(1);
			} else {
				Long value = fibonnaci(n - 1) + fibonnaci(n - 2);
				fibonnaciSequenceMap.put(n, value);
				fibonacciNumbers.add(value);
				return value;
			}
		}

		public static Fibonacci getInstance() {
			if (instance == null) {
				instance = new Fibonacci();
			}
			return instance;
		}
	}
}
