<?php 

loadControllerTest();

class ArticlesControllerTestCase extends UnitTestCase
{
	var $object = null;

	function setUp()
	{
		$this->object = new Articles();
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