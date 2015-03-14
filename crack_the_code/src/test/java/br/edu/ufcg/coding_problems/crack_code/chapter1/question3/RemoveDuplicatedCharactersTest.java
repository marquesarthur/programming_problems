package br.edu.ufcg.coding_problems.crack_code.chapter1.question3;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class RemoveDuplicatedCharactersTest {

	@Test(expected = RuntimeException.class)
	public void testRemoveDuplicatesFromNullString() {
		RemoveDuplicatedCharacters.removeDuplicates(null);
	}

	@Test
	public void testRemoveDuplicatesFromEmptyString() {
		String in = "";
		String out = RemoveDuplicatedCharacters.removeDuplicates(in);

		Assert.assertEquals(in, out);
	}

	@Test
	public void testRemoveDuplicatesFromSingleCharacterString() {
		String in = "a";
		String out = RemoveDuplicatedCharacters.removeDuplicates(in);

		Assert.assertEquals(in, out);
	}

	@Test
	public void testRemoveDuplicatesFromNonDuplicatedString() {
		String in = "abcde";
		String out = RemoveDuplicatedCharacters.removeDuplicates(in);

		Assert.assertEquals(in, out);
	}

	@Test
	public void testRemoveDuplicatesFromOneDuplicatedCharacterString() {
		String in = "abaacdea";
		String out = RemoveDuplicatedCharacters.removeDuplicates(in);

		Assert.assertEquals("abcde", out);
	}

	@Test
	public void testRemoveDuplicatesFromTwoDuplicatedCharacterString() {
		String in = "ababacdeabb";
		String out = RemoveDuplicatedCharacters.removeDuplicates(in);

		Assert.assertEquals("abcde", out);
	}
}
