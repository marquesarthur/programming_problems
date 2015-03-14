package br.edu.ufcg.coding_problems.crack_code.chapter4.question2;

import br.edu.ufcg.coding_problems.crack_code.chapter4.TreeNode;

public class ArrayToTree {
	
	public static TreeNode getTree(Integer[] array){
		
		if (array == null) {
			throw new RuntimeException("Cannot iterate null array");
		} else if (array.length == 0){
			throw new RuntimeException("Cannot iterate empty array");
		}
		
		int middle = array.length / 2;
		TreeNode root = new TreeNode(array[middle]);
		
		traverseArray(root, array, 0, middle - 1);
		traverseArray(root, array, middle + 1, array.length - 1);
		
		return root;
	}

	private static void traverseArray(TreeNode currentNode, Integer[] array, int begin, int end) {
		if (begin < 0 || begin > array.length || end > array.length){
			return;
		} else if (begin > end){
			return;
		} else {
			int middle = (begin + end) / 2;
			
			currentNode.insert(array[middle]);
			traverseArray(currentNode, array, begin, middle - 1);
			traverseArray(currentNode, array, middle + 1, end);
		}
	}
	
	
	
//public static TreeNode getTree(Integer[] array) {
//		
//		if (array == null){
//			throw new RuntimeException();
//		} else if (array.length == 0){
//			throw new RuntimeException();
//		}
//
//		return getTree(array, 0, array.length - 1);
//	}
//
//	private static TreeNode getTree(Integer[] array, int begin, int end) {
//		if (begin > end) {
//			return null;
//		} else {
//			int middle = (begin + end) / 2;
//
//			TreeNode root = new TreeNode(array[middle]);
//
//			root.left = getTree(array, begin, middle - 1);
//			root.right = getTree(array, middle + 1, end);
//
//			return root;
//
//		}
//	}

}
