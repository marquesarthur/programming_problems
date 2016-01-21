package br.edu.ufcg.coding_problems.crack_code.chapter8.question7;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class PossibleCentRepresentationsTest {

	@Test
	public void testPossibleRepresentationsOfOneCent() {
		List<List<Integer>> possibleCents = PossibleCentRepresentations
				.getPossibleCents(1);

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		List<Integer> possibleRepresentation = Arrays
				.asList(new Integer[] { 1 });
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);

		Assert.assertFalse(possibleCents.isEmpty());

		for (List<Integer> currentRepresentation : possibleCents) {
			Assert.assertTrue(expected.contains(currentRepresentation));
			expected.remove(currentRepresentation);
		}
	}
	
	
	@Test
	public void testPossibleRepresentationsOfFiveCents() {
		List<List<Integer>> possibleCents = PossibleCentRepresentations
				.getPossibleCents(5);

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		List<Integer> possibleRepresentation = Arrays
				.asList(new Integer[] { 1, 1, 1, 1, 1 });
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);
		
		possibleRepresentation = Arrays
				.asList(new Integer[] {5});
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);

		Assert.assertFalse(possibleCents.isEmpty());

		Assert.assertEquals(expected, possibleCents);
	}
	
	
	@Test
	public void testPossibleRepresentationsOfTenCents() {
		List<List<Integer>> possibleCents = PossibleCentRepresentations
				.getPossibleCents(10);

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		List<Integer> possibleRepresentation = Arrays
				.asList(new Integer[] { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 });
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);
		
		possibleRepresentation = Arrays
				.asList(new Integer[] {1, 1, 1, 1, 1, 5});
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);
		
		possibleRepresentation = Arrays
				.asList(new Integer[] {5, 5});
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);
		
		possibleRepresentation = Arrays
				.asList(new Integer[] {10});
		Collections.sort(possibleRepresentation);
		expected.add(possibleRepresentation);

		Assert.assertFalse(possibleCents.isEmpty());

		Assert.assertEquals(expected, possibleCents);
	}
	
}
