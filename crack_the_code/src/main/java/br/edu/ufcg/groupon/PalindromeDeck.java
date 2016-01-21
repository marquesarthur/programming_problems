package br.edu.ufcg.groupon;

import java.io.*;
import java.util.*;

public class PalindromeDeck {

	private static final String COMA = ",";

	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String deckFront = "aaaaaaaaaaaa,nopalindrome,steponnopets,emordnilapon,aaaaaaaaaaaa,steponnopets,nopalindrome,steponnopets,nopalindrome,bbbbbbbbbbbb,cannotbeused,cannotbeused,steponnopets,aaaaaaaaaaaa,nopalindrome,aaaaaaaaaaaa,nopalindrome,emordnilapon,steponnopets,nopalindrome"; // in.readLine();
		String deckBack = "4096,131072,64,262144,512,1024,65536,2048,32768,1,524288,16384,32,4,16,2,8,128,8192,256"; // in.readLine();

		String[] fronts = deckFront.split(COMA);
		String[] backs = deckBack.split(COMA);

		List<Card> deck = buildDeck(fronts, backs);

		List<List<Card>> allDeckCombinations = new LinkedList<List<Card>>();
		for (int i = 1; i <= deck.size(); i++) {
			allDeckCombinations.addAll(combination(deck, i));
		}

		List<List<Card>> palindromeDecks = new LinkedList<List<Card>>();

		for (List<Card> combination : allDeckCombinations) {
			List<List<Card>> palindromeHand = permute(combination);
			if (!palindromeHand.isEmpty()) {
				palindromeDecks.addAll(palindromeHand);
			}
		}

		long greatesvalue = getGreatestDeckScore(palindromeDecks);
		System.out.println(greatesvalue);
	}

	/**
	 * Search with the palindrome decks, which one has the greates score
	 * @param palindromeDecks - to be searched
	 * @return greatest deck score value
	 */
	private static long getGreatestDeckScore(List<List<Card>> palindromeDecks) {
		long greatestScore = Long.MIN_VALUE;
		for (List<Card> palindromeHand : palindromeDecks) {
			long deckScore = getDeckScore(palindromeHand);
			if (deckScore > greatestScore) {
				greatestScore = deckScore;
			}
		}

		// this check if there is no palindrome deck at all
		if (greatestScore == Long.MIN_VALUE) {
			greatestScore = 0;
		}
		return greatestScore;
	}

	/**
	 * Sum all cards back values within a deck
	 * @param hand - to be summed
	 * @return deck back sum
	 */
	private static long getDeckScore(List<Card> hand) {
		long sum = 0;
		for (Card card : hand) {
			sum += card.getBack();
		}
		return sum;
	}

	/**
	 * Check if a hand of cards is palindrome
	 * @param hand - to be checked
	 * @return true if the hand is palindrome. false otherwise
	 */
	private static boolean isPalindrome(List<Card> hand) {
		StringBuffer str = new StringBuffer();
		for (Card card : hand) {
			str.append(card.getFront());
		}

		return isPalindrome(str.toString());
	}

	/**
	 * Check if a string is palindrome
	 * @param string - to be checked
	 * @return true if the string is palindrome. false otherwise
	 */
	private static boolean isPalindrome(String string) {
		String reverse = new StringBuffer(string).reverse().toString();

		if (reverse.equals(string)) {
			return true;
		}

		return false;
	}

	/**
	 * Get all possible combinations of cards within a deck
	 * @param deck
	 * @param deckSize
	 * @return list of possible combinations of cards within a deck
	 */
	public static List<List<Card>> combination(List<Card> deck, int deckSize) {

		if (0 == deckSize) {
			return Collections.singletonList(Collections.<Card> emptyList());
		}

		if (deck.isEmpty()) {
			return Collections.emptyList();
		}

		List<List<Card>> combination = new LinkedList<List<Card>>();
		Card currentCard = deck.iterator().next();
		List<Card> remainder = new LinkedList<Card>(deck);
		remainder.remove(currentCard);

		List<List<Card>> remainderCombination = combination(remainder,
				deckSize - 1);

		for (List<Card> set : remainderCombination) {
			List<Card> newSet = new LinkedList<Card>(set);
			newSet.add(0, currentCard);
			combination.add(newSet);
		}

		combination.addAll(combination(remainder, deckSize));

		return combination;
	}

	/**
	 * Creates a deck of cards containing the card front and back
	 * 
	 * @param fronts
	 * 		Array containing all the fronts of all the cards
	 * @param backs
	 * 		Array containing all the backs of all the cards
	 * @return
	 * 		List of cards
	 */
	private static List<Card> buildDeck(String[] fronts, String[] backs) {
		List<Card> deck = new ArrayList<Card>();
		for (int i = 0; i < fronts.length; i++) {
			deck.add(new Card(fronts[i], Long.valueOf(backs[i])));
		}
		return deck;
	}

	
	/**
	 * Gets all the possible permutations of cards within a deck.
	 * Only palindrome hands are returned
	 * 
	 * @param hand - to be permuted
	 * @return palindrome sequences of cards
	 */
	public static List<List<Card>> permute(List<Card> hand) {
		List<List<Card>> permutations = new LinkedList<List<Card>>();
		permute(hand, 0, permutations);
		return permutations;
	}

	static void permute(List<Card> hand, int start,
			List<List<Card>> permutations) {

		if (start >= hand.size()) {
			if (isPalindrome(hand)) {
				permutations.add(hand);
			}
		}

		for (int j = start; j <= hand.size() - 1; j++) {
			swap(hand, start, j);
			permute(hand, start + 1, permutations);
			swap(hand, start, j);
		}
	}

	private static void swap(List<Card> hand, int i, int j) {
		Card temp = new Card(hand.get(i));
		hand.get(i).copy(hand.get(j));
		hand.get(j).copy(temp);
	}
	
	/**
	 * Auxiliary class that encapsulates a card
	 * A card contains a front and a back
	 * 
	 * It was necessacy to declare the class as static. Although, in a real project we could import it from a pojo package
	 * 
	 */
	private static class Card {

		public String getFront() {
			return front;
		}

		public long getBack() {
			return back;
		}

		private String front;

		private long back;

		/**
		 * Default constructor
		 * 
		 * @param front - of the card
		 * @param back - back of the card
		 */
		public Card(String front, long back) {
			this.front = front;
			this.back = back;
		}

		/**
		 * Constructor based on a card to be copied
		 * @param card - to be copied
		 */
		public Card(Card card) {
			this.front = card.getFront();
			this.back = card.getBack();
		}

		/**
		 * Copy the front and back of a card into another
		 * @param card - to be copied
		 */
		public void copy(Card card) {
			this.front = card.getFront();
			this.back = card.getBack();
		}
		
		public String toString() {
			return String.format("%s:%s", front, back);
		}
	}
}
