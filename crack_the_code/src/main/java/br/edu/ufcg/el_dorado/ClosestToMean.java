package br.edu.ufcg.el_dorado;

import java.io.*;

class ClosestToMean {
	
public static final String WHITE_SPACE = " ";
	
	private static String[] getNumbers(BufferedReader br) throws IOException {
		String array = br.readLine();
		String[] numbersInArray = array.trim().split(WHITE_SPACE);
		return numbersInArray;
	}
	
	private static int getNumberOfElements(BufferedReader br)
			throws IOException {
		String nParam = br.readLine();
		int n = Integer.parseInt(nParam);
		return n;
	}
	
	private static long getClosestToMean(int n, String[] numbersInArray) {
		long sum = 0;
		
		for (String currentNumber: numbersInArray) {
			sum += Long.parseLong(currentNumber);
		}
		
		long closestToMean = sum / n;
		return closestToMean;
	}
	
	public static void main(String[] args) throws java.lang.Exception {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int n = getNumberOfElements(br);

			String[] numbersInArray = getNumbers(br); 
			long closestToMean = getClosestToMean(n, numbersInArray);
			
			System.out.println(closestToMean);
		} catch (Exception ex) {
			System.out.println(0);
		}
	}
}
