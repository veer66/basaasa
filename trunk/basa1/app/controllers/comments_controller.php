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

class CommentsController extends AppController
{
	//var $scaffold;
	var $name = 'Comments';
	var $uses = array('Comment', 'Article', 'User');
	var $helpers = array('Html', 'Form' , 'Time');

     function beforeFilter() {
         $this->checkSession();
     }


	function index($article_id) {
		$this->Comment->recursive = 0;
        $this->data = array('Comment' => array('article_id' => $article_id));
		$this->set('comments', $this->Comment->findAll("article_id = " . $article_id));
	}

	function add() {
		if(empty($this->data)) {
			$this->set('articleArray', $this->Comment->Article->generateList());
			$this->set('userArray', $this->Comment->User->generateList());
			$this->render();
		} else {
			$this->cleanUpFields();
            $this->data['Comment']['timestamp'] = time();
            //FIXME: check valid article?
            $this->data['Comment']['user_id'] = $this->getUserId();
            
			if($this->Comment->save($this->data)) {
				$this->Session->setFlash('The Comment has been saved');
				$this->redirect('/comments/index/' . $this->data['Comment']['article_id']);
			} else {				
				$this->set('articleArray', $this->Comment->Article->generateList());
				$this->set('userArray', $this->Comment->User->generateList());
				$this->Session->setFlash('Please correct errors below.');
				$this->redirect('/comments/index/' . $this->data['Comment']['article_id']);
			} 
		}
	}

}
?>