<?php

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

 
class User extends AppModel
{
    var $name = 'User';
    var $belongsTo = array('Group');
    var $hasMany = array('Translation', 'Reservation');
	var $validate = array('username' => VALID_NOT_EMPTY,
						  'password' => VALID_NOT_EMPTY,
						  'first_name' => VALID_NOT_EMPTY,
						  'last_name' => VALID_NOT_EMPTY,
						  'email' => VALID_EMAIL);
}
?>
