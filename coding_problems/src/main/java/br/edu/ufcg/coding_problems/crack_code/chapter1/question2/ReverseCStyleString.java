package br.edu.ufcg.coding_problems.crack_code.chapter1.question2;

public class ReverseCStyleString {

	public static Character[] revert(Character[] in) {
		
		if (in == null){
			throw new RuntimeException("Cannot revert null string");
		}
		
		if (in.length == 0){
			throw new RuntimeException("Cannot revert completly empty string, which has no eof character");
		}
		
		if (in.length <= 2){
			return in;
		}
		
		int endOfString = in.length - 2;
		int current = 0;
		
		for (int i = endOfString; i >= current; i--){
			char swap = in[current];
			in[current] = in[i];
			in[i] = swap;
			current++;
		}
		
		for (int i = 0; i < in.length; i++) {
			System.out.print(in[i]);
		}
		
		return in;
	}

}
