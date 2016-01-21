package br.edu.ufcg.coding_problems.crack_code.chapter8.question7;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PossibleCentRepresentations {

	private static final Integer ONE_CENT = 1;
	private static final Integer FIVE_CENTS = 5;
	private static final Integer TEN_CENTS = 10;
	private static final Integer TWENTY_FIVE_CENTS = 25;

	public static List<List<Integer>> getPossibleCents(Integer value) {

		List<List<Integer>> possibleRepresentations = new ArrayList<List<Integer>>();

		List<Integer> possibleCoins = getCoinsForValue(value);

		for (Integer coin : possibleCoins) {
			addCoin(0, coin, value, possibleRepresentations,
					new ArrayList<Integer>());
		}

		return possibleRepresentations;

	}

	private static void addCoin(int currentValue, Integer coin, Integer value,
			List<List<Integer>> possibleRepresentations,
			ArrayList<Integer> currentCoinSack) {

		currentValue = currentValue + coin;

		if (currentValue == value) {
			currentCoinSack.add(coin);
			Collections.sort(currentCoinSack);
			if (!possibleRepresentations.contains(currentCoinSack)) {
				possibleRepresentations.add(currentCoinSack);
			}
		} else if (currentValue > value) {
			return;
		} else {
			currentCoinSack.add(coin);
			List<Integer> possibleCoins = getCoinsForValue(value - currentValue);
			for (Integer newCoin : possibleCoins) {
				addCoin(currentValue, newCoin, value, possibleRepresentations,
						new ArrayList<Integer>(currentCoinSack));
			}
		}
	}

	private static List<Integer> getCoinsForValue(Integer value) {

		List<Integer> result = new ArrayList<Integer>();

		if (value > 0) {
			result.add(ONE_CENT);
		}
		if (value >= 5) {
			result.add(FIVE_CENTS);
		}
		if (value >= 10) {
			result.add(TEN_CENTS);
		}
		if (value >= 25) {
			result.add(TWENTY_FIVE_CENTS);
		}

		return result;
	}
}
