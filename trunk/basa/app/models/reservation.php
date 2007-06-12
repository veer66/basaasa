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

 
class Reservation extends AppModel 
{
    var $name = 'Reservation';
    var $belongsTo = array('Article', 'User');

	function delByArticleIdAndUserId($article_id, $user_id) {
		$prefix = $this->tablePrefix;
		$table_name = $this->useTable;
		
		// FIXME: Is there better technique to check the error?
		if(count($this->execute("delete from $prefix" . "$table_name where article_id = $article_id and user_id = $user_id")) == 0) {
			return true;
		} else {
			return false;
		}
	}
}
?>
