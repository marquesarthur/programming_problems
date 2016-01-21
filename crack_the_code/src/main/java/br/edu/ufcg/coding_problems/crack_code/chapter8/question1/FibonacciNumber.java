package br.edu.ufcg.coding_problems.crack_code.chapter8.question1;

import java.util.HashMap;
import java.util.Map;

public class FibonacciNumber {
	
	private static  FibonacciNumber instance;
	
	private Map<Integer, Integer> mapNthValue;
	
	private FibonacciNumber(){
		mapNthValue = new HashMap<Integer, Integer>();
		
		mapNthValue.put(0, 0); // the first Fibonacci number is 1 
		mapNthValue.put(1, 1); // the second Fibonacci number is also 1
	}
	
	public static FibonacciNumber getInstance(){
		if (instance == null){
			instance = new FibonacciNumber();
		}
		return instance;
	}

	public Integer get(Integer n) {

		if (mapNthValue.containsKey(n)){
			return mapNthValue.get(n);
		} 
		
		Integer value = get(n - 1) + get (n - 2);
		mapNthValue.put(n, value);
		
		return value;
	}

}
