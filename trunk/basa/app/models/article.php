<?
//	Copyright (c) 2006 - 2007  Vee Satayamas <vsatayamas@gmail.com>
//	All rights reserved.
//
//	This file is part of Basa-Asa.
//
//  Basa-Asa is free software; you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation; either version 2 of the License, or
//  (at your option) any later version.
//
//  Basa-Asa is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with Basa-Asa; if not, write to the Free Software
//  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 
class Article extends AppModel
{
    var $name = 'Article';
	var $displayField = 'id'; // FIXME: title must be displayed instead of id?
    var $hasMany = array('Translation' => array('order' => 'revision desc'),
                         'Comment' => array('order' => 'timestamp desc'),
						 'Reservation' 
                         );

	function findNormal() {
		return $this->findAll('deleted = 0', null, "id DESC");
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

			// $article['Article']['reserved'] = $status['Article']['reserved'];
			$article['Article']['need_checking'] = $status['Article']['need_checking'];
			return $this->save($article);
		} 
		return false;		
	}
}
?>
