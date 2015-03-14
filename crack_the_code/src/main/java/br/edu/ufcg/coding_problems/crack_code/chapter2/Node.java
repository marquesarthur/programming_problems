package br.edu.ufcg.coding_problems.crack_code.chapter2;

import java.util.ArrayList;
import java.util.List;

public class Node {

	private int value;

	private Node next;

	public Node(int value) {
		this.value = value;
		this.next = null;
	}

	public Node() {
	}

	public void append(int value) {

		Node current = this;

		while (current.getNext() != null) {
			current = current.getNext();
		}
		current.setNext(new Node(value));
	}

	public int getValue() {
		return value;
	}

	public void setValue(int value) {
		this.value = value;
	}

	public Node getNext() {
		return next;
	}

	public void setNext(Node next) {
		this.next = next;
	}

	public Node delete(Node head, int value) {
		Node current = this;

		if (current.getValue() == value) {
			return current.getNext();
		}

		while (current.getNext() != null) {
			if (current.getNext().getValue() == value) {
				current.setNext(current.getNext().getNext());
			}
			current = current.getNext();
		}
		return head;
	}

	public List<Integer> toList() {
		List<Integer> result = new ArrayList<Integer>();

		Node current = this;

		while (current != null) {
			result.add(new Integer(current.getValue()));
			current = current.getNext();
		}
		return result;
	}
}
