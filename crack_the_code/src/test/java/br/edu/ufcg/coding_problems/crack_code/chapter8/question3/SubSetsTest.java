package br.edu.ufcg.coding_problems.crack_code.chapter8.question3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class SubSetsTest {

	@Test
	public void testSubSetsOfEmpty() {

		List<List<Integer>> allSubSets = SubSets
				.getAllSubSets(new ArrayList<Integer>());

		Assert.assertTrue(allSubSets.isEmpty());
	}

	@Test
	public void testSubSetsOfOneElementSet() {

		List<List<Integer>> allSubSets = SubSets.getAllSubSets(Arrays
				.asList(new Integer[] { 1 }));

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		expected.add(Arrays.asList(new Integer[] { 1 }));

		Assert.assertFalse(allSubSets.isEmpty());
		Assert.assertEquals(expected, allSubSets);
	}

	@Test
	public void testSubSetsOfTwoElementsSet() {

		List<List<Integer>> allSubSets = SubSets.getAllSubSets(Arrays
				.asList(new Integer[] { 1, 2 }));

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		expected.add(Arrays.asList(new Integer[] { 1 }));
		expected.add(Arrays.asList(new Integer[] { 2 }));
		expected.add(Arrays.asList(new Integer[] { 1, 2 }));

		Assert.assertFalse(allSubSets.isEmpty());
		for (List<Integer> subSet : allSubSets) {
			Assert.assertTrue(expected.contains(subSet));
			expected.remove(subSet);
		}
		Assert.assertTrue(expected.isEmpty());
	}

	@Test
	public void testSubSetsOfThreeElementsSet() {

		List<List<Integer>> allSubSets = SubSets.getAllSubSets(Arrays
				.asList(new Integer[] { 1, 2, 3 }));

		List<List<Integer>> expected = new ArrayList<List<Integer>>();
		expected.add(Arrays.asList(new Integer[] { 1 }));
		expected.add(Arrays.asList(new Integer[] { 2 }));
		expected.add(Arrays.asList(new Integer[] { 3 }));
		expected.add(Arrays.asList(new Integer[] { 1, 2 }));
		expected.add(Arrays.asList(new Integer[] { 1, 3 }));
		expected.add(Arrays.asList(new Integer[] { 2, 3 }));
		expected.add(Arrays.asList(new Integer[] { 1, 2, 3 }));

		Assert.assertFalse(allSubSets.isEmpty());
		for (List<Integer> subSet : allSubSets) {
			Assert.assertTrue(expected.contains(subSet));
			expected.remove(subSet);
		}
		Assert.assertTrue(expected.isEmpty());
	}

}
