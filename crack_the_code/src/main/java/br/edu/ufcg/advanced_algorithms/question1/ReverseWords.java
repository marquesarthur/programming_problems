package br.edu.ufcg.advanced_algorithms.question1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReverseWords {

	public static void main(String args[]) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		
		while ((input = br.readLine()) != null) {
			StringBuilder str = new StringBuilder();
			String[] words = input.split(" ");
			for (int i = words.length - 1; i >= 0; i--){
				str.append(words[i]);
				str.append(" ");
			}
			System.out.println(str.toString().trim());
		}
	}
}
