package br.edu.ufcg.coding_problems.crack_code.chapter1.question2;

import junit.framework.Assert;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class ReverseCStyleStringTest {

	@Test
	public void testReverseValidSingleCharacterString() {
		Character[] in = { 'a', null };
		Character[] out = { 'a', null };

		Assert.assertTrue(isEqual(out, ReverseCStyleString.revert(in)));
	}

	@Test
	public void testReverseValidPairSizeString() {
		Character[] in = { 'a', 'b', 'c', 'd', null };
		Character[] out = { 'd', 'c', 'b', 'a', null };

		Assert.assertTrue(isEqual(out, ReverseCStyleString.revert(in)));
	}

	@Test
	public void testReverseValidEvenSizeString() {
		Character[] in = { 'a', 'b', 'c', null };
		Character[] out = { 'c', 'b', 'a', null };

		Assert.assertTrue(isEqual(out, ReverseCStyleString.revert(in)));
	}

	@Test(expected = RuntimeException.class)
	public void testReverseNullString() {
		ReverseCStyleString.revert(null);
	}

	@Test(expected = RuntimeException.class)
	public void testReverseEmpyInvalidString() {
		Character[] in = {};
		ReverseCStyleString.revert(in);
	}

	@Test
	public void testReverseEmpyValidString() {
		Character[] in = { null };
		Character[] out = { null };
		Assert.assertTrue(isEqual(out, ReverseCStyleString.revert(in)));
	}

	private boolean isEqual(Character[] out, Character[] revert) {
		for (int i = 0; i < revert.length - 1; i++) {
			if (out[i] != revert[i]) {
				return false;
			}
		}
		return true;
	}
}
