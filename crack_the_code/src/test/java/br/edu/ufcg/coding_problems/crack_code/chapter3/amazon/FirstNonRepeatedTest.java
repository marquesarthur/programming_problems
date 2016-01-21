package br.edu.ufcg.coding_problems.crack_code.chapter3.amazon;

import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class FirstNonRepeatedTest {

	private FirstNonRepeated buffer;

	@Before
	public void setUp() {
		this.buffer = new FirstNonRepeated();
	}

	@Test
	public void testFisrtNonRepeated1() {
		this.buffer.push(new Character('a'));

		Assert.assertEquals(new Character('a'),
				this.buffer.getlastNonRepeated());
	}

	@Test
	public void testFisrtNonRepeated2() {
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('a'));

		Assert.assertEquals(null, this.buffer.getlastNonRepeated());
	}

	@Test
	public void testFisrtNonRepeated3() {
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('a'));

		Assert.assertEquals(new Character('b'),
				this.buffer.getlastNonRepeated());
	}

	@Test
	public void testFisrtNonRepeated4() {
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));

		Assert.assertEquals(null, this.buffer.getlastNonRepeated());
	}

	@Test
	public void testFisrtNonRepeated5() {
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('c'));

		Assert.assertEquals(new Character('c'),
				this.buffer.getlastNonRepeated());
	}

	@Test
	public void testFisrtNonRepeated6() {
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('a'));
		this.buffer.push(new Character('b'));
		this.buffer.push(new Character('c'));
		this.buffer.push(new Character('a'));

		Assert.assertEquals(new Character('c'),
				this.buffer.getlastNonRepeated());
	}

}
