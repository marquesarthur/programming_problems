package br.edu.ufcg.coding_problems.crack_code.chapter8.question4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class StringPermutationTest {

	@Test(expected = RuntimeException.class)
	public void testPermuteNullString() {
		StringPermutation.getPermutations(null);
	}

	@Test
	public void testPermuteEmptyString() {
		List<String> permutations = StringPermutation.getPermutations("");

		List<String> expected = new ArrayList<String>();
		expected.add("");

		Assert.assertEquals(expected, permutations);
	}

	@Test
	public void testPermuteSingleCharacterString() {
		List<String> permutations = StringPermutation.getPermutations("a");

		List<String> expected = new ArrayList<String>();
		expected.add("a");

		Assert.assertEquals(expected, permutations);
	}

	@Test
	public void testPermuteDoubleCharacterString() {
		List<String> permutations = StringPermutation.getPermutations("ab");

		List<String> expected = Arrays.asList(new String[] {"ba", "ab"});
		Collections.sort(expected);

		Collections.sort(permutations);
		Assert.assertEquals(expected, permutations);
	}

	@Test
	public void testPermuteFourCharacterString() {
		List<String> permutations = StringPermutation.getPermutations("abc");

		List<String> expected = Arrays.asList(new String[] { "abc", "bac",
				"bca", "acb", "cab", "cba" });

		Collections.sort(expected);

		System.out.println(expected);
		System.out.println(permutations);

		Collections.sort(permutations);
		Assert.assertEquals(expected, permutations);
	}
}
