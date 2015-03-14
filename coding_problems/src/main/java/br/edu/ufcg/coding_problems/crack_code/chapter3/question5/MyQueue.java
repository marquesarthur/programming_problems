package br.edu.ufcg.coding_problems.crack_code.chapter3.question5;

import br.edu.ufcg.coding_problems.crack_code.chapter2.Node;
import br.edu.ufcg.coding_problems.crack_code.chapter3.Stack;

public class MyQueue {
	
	private Stack a;
	private Stack b;
	
	
	public MyQueue() {
		a = new Stack();
		b = new Stack();
		
	}
	
	public void push(Node node){
		if (!a.isEmpty()){
			a.push(node);
		} else if (!b.isEmpty()){
			b.push(node);
		} else {
			a.push(node);
		}
	}
	
	public Node pop(){
		if (a.isEmpty()) {
			return popFromTo(b, a); 
		} else {
			return popFromTo(a, b);
		}
	}

	private Node popFromTo(Stack from, Stack to) {
		
		while(!from.isEmpty()){
			Node node = from.pop();
			to.push(node);
		}
		
		return to.pop();
	}

}
