package br.edu.ufcg.el_dorado;

import java.io.*;

class SumDigits {
	public static void main(String[] args) throws java.lang.Exception {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			for (String line = null; (line = br.readLine()) != null;) {
				int output = 0;
				for (Character c : line.toCharArray()) {
					output += Integer.parseInt(c.toString());
				}
				System.out.println(output);
			}
		} catch (Exception ex) {
			System.out.println(0);
		}
	}
}
