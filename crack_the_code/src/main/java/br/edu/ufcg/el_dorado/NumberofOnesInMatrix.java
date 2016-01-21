package br.edu.ufcg.el_dorado;

import java.io.BufferedReader;
import java.io.InputStreamReader;


class NumberofOnesInMatrix {
	public static void main(String[] args) throws java.lang.Exception {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			Integer n = Integer.parseInt(br.readLine());
			Matrix matrix = new Matrix(n);
			
			int i = 0;
			for (String line = null; (line = br.readLine()) != null;) {
				if (line.isEmpty()){
					break;
				}
				matrix.addLine(line, i);
				i++;
			}
			matrix.NumberOfAdjacentOnes();
		} catch (Exception ex) {
			System.out.println(0);
		}
	}

	static class Matrix {
		
		private static final String WHITE_SPACE = " ";

		private int matrix[][];
		
		private int MAX_N = 1000;

		private int n;
		
		public Matrix(int n) {
			if (n > MAX_N) {
				throw new RuntimeException("Error max size is 1000 x 1000");
			}
			this.n = n;
			this.matrix = new int[n][n];
		}
		
		public void NumberOfAdjacentOnes() {
			for (int i = 0; i < n; i++) {
				StringBuffer line = new StringBuffer();
				for (int j = 0; j < n; j++) {
					line.append(WHITE_SPACE);
					int adjacentOnes = getNumberOfAdjacentOnes(i, j);
					line.append(adjacentOnes);
				}
				System.out.println(line.toString().trim());
			}
		}

		private int getNumberOfAdjacentOnes(int i, int j) {
			int numberOfOnes = 0;
			// line before
			numberOfOnes += hasOneAt(i-1, j -1);
			numberOfOnes += hasOneAt(i-1, j);
			numberOfOnes += hasOneAt(i-1, j + 1);
			// current line
			numberOfOnes += hasOneAt(i, j-1);
			numberOfOnes += hasOneAt(i, j+1);
			// next line
			numberOfOnes += hasOneAt(i+1, j-1);
			numberOfOnes += hasOneAt(i+1, j);
			numberOfOnes += hasOneAt(i+1, j+1);

			return numberOfOnes;
		}

		private int hasOneAt(int i, int j) {
			if (i < 0 || j < 0) {
				return 0;
			}
			if (i >= n || j >= n) {
				return 0;
			}
			return matrix[i][j];
		}

		public void addLine(String input, int i) {
			String[] numbersInArray = input.trim().split(WHITE_SPACE);
			for (int j = 0; j < n; j++) {
				matrix[i][j] = Integer.valueOf(numbersInArray[j]);
			}
		}
	}
}
