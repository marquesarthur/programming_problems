package br.edu.ufcg.coding_problems.crack_code.chapter2.question1;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;

public class RemoveDuplicates {
	
	public static Node removeDuplicates(Node head){
		if (head == null){
			throw new RuntimeException("Cannot remove duplicates from null linked list");
		}
		
		Node current = head;
		
		while (current != null && current.getNext() != null){
			Node searchDuplicate = current;
			
			while (searchDuplicate != null && searchDuplicate.getNext() != null){
				
				if (searchDuplicate.getNext().getValue() == current.getValue()){
					searchDuplicate.setNext(searchDuplicate.getNext().getNext());
				} else { 
					searchDuplicate = searchDuplicate.getNext();
				}				
			}
			current = current.getNext();
		}
		
		return head;
	}
}
