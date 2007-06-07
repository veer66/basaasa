<?
/* 
 * Basa-Asa: A web-based collaborative translation platform
 *
 * Copyright (C) 2006  Vee Satayamas
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */
 
class Article extends AppModel
{
    var $name = 'Article';
    var $hasMany = array('Translation' => 
                         array('order' => 'revision desc'),
                         'Comment' =>
                         array('order' => 'timestamp desc')
                         );

	function findNormal() {
		return $this->findAll('deleted = 0');
	}
	
	function lazyDel($id) {
		$d = $this->read(null, $id);		
		if($d) {
			$d['Article']['deleted'] = 1;
			return $this->save($d);
		}
		return false;
	}
	
	function save_status($id, $status) {
		$article = $this->read(null, $id);
		if($article) {

			$article['Article']['reserved'] = $status['Article']['reserved'];
			$article['Article']['need_checking'] = $status['Article']['need_checking'];
			return $this->save($article);
		} 
		return false;		
	}
}
?>
