package br.edu.ufcg.coding_problems.crack_code.chapter8.question1;


import junit.framework.Assert;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;


@RunWith(JUnit4.class)
public class FibonacciNumberTest {
	
	private  FibonacciNumber fibonacci;
	
	@Before
	public void setUp(){
		fibonacci = FibonacciNumber.getInstance();
	}
	
	
	@Test
	public void testFirstNumber(){
		Integer valueOfNth = fibonacci.get(1);
		Assert.assertEquals(new Integer(1), valueOfNth);
	}
	
	@Test
	public void testSecondNumber(){
		Integer valueOfNth = fibonacci.get(2);
		Assert.assertEquals(new Integer(1), valueOfNth);
	}
	
	@Test
	public void testThirdNumber(){
		Integer valueOfNth = fibonacci.get(3);
		Assert.assertEquals(new Integer(2), valueOfNth);
	}
	
	@Test
	public void testEighthNumber(){
		Integer valueOfNth = fibonacci.get(8);
		Assert.assertEquals(new Integer(21), valueOfNth);
	}

}
