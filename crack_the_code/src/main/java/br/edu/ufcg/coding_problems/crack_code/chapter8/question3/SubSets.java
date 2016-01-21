package br.edu.ufcg.coding_problems.crack_code.chapter8.question3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SubSets {

	public static List<List<Integer>> getAllSubSets(List<Integer> set) {

		List<List<Integer>> allSets = new ArrayList<List<Integer>>();
		
		extractSubSets(set.size() - 1, set, allSets);
		
		
		for (List<Integer> subSet: allSets){
			Collections.sort(subSet);
		}
		
		return allSets;
	}

	private static void extractSubSets(int currentIndex, 
			List<Integer> set, List<List<Integer>> allSets) {
		
		
		if (currentIndex >= 0){
			List<Integer> currentSet = new ArrayList<Integer>();
			Integer value = set.get(currentIndex);
			currentSet.add(value);
			
			List<List<Integer>> auxSets = new ArrayList<List<Integer>>();
			for (List<Integer> subSet : allSets){
				List<Integer> aux = new ArrayList<Integer>();
				aux.addAll(subSet);
				aux.add(value);
				auxSets.add(aux);
			}
			if (!auxSets.isEmpty()){
				allSets.addAll(auxSets);
			}
			
			allSets.add(currentSet);
			
			currentIndex--;
			extractSubSets(currentIndex, set, allSets);
		}
	}
}
