<?php 

loadControllerTest();

class TranslationsControllerTestCase extends UnitTestCase
{
	var $object = null;

	function setUp()
	{
		$this->object = new Translations();
	}

	function tearDown()
	{
		unset($this->object);
	}

	/*
	function testMe()
	{
		$result = $this->object->doSomething();
		$expected = 1;
		$this->assertEquals($result, $expected);
	}
	*/
}
?>