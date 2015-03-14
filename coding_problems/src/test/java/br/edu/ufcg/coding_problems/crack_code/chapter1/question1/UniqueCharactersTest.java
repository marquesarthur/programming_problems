package br.edu.ufcg.coding_problems.crack_code.chapter1.question1;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class UniqueCharactersTest {

	@Test
	public void testUniqueValidString() {
		Assert.assertTrue(UniqueCharacters.isUnique("abcdefgh"));
	}

	@Test
	public void testUniqueInvalidString() {
		Assert.assertFalse(UniqueCharacters.isUnique("aaabcdefghijk"));
	}

	@Test(expected = RuntimeException.class)
	public void testUniqueNullString() {
		UniqueCharacters.isUnique(null);
	}

	@Test
	public void testUniqueEmptyString() {
		Assert.assertTrue(UniqueCharacters.isUnique(""));
	}
}
