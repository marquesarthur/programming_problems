package br.edu.ufcg.coding_problems.crack_code.chapter2.question3;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class DeleteFromMiddle {
	
	
	public static void delete(Node current){
		current.setValue(current.getNext().getValue());
		current.setNext(current.getNext().getNext());
	}
}
