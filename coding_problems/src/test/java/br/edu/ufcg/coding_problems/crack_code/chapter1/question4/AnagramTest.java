package br.edu.ufcg.coding_problems.crack_code.chapter1.question4;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class AnagramTest {

	@Test
	public void testAnagramForValidString() {
		Assert.assertTrue(Anagram.isAnagram("Alan Smithee", "The alias men"));
	}

}
