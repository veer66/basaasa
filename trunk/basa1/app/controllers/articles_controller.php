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


class ArticlesController extends AppController
{
    
	//var $scaffold;
	var $name = 'Articles';
	var $helpers = array('Html', 'Form' , 'Text', 'Javascript');


    function index() {
		
        $this->Article->recursive = 1;
        $this->set('articles', $this->Article->findNormal());
    }

    function delete($id) {
		$this->checkAdmin();
        
       	if($this->Article->lazyDel($id)) {
            $this->Session->setFlash('The Article deleted: id '.$id.'');
            $this->redirect('/');
        } 
    }

    function update($id) {
		$this->checkAdmin();
        $this->Article->save($this->data);
        $this->redirect('/articles/view/' . $id);
    }

	function status_update($id) {
		$this->checkSession();
        $this->Article->save_status($id, $this->data);
        $this->redirect('/articles/view/' . $id);
    }
    
    function add() {
        $this->checkAdmin();
        if(empty($this->data)) {
            $this->render();
        } else {
            $this->cleanUpFields();
            if($this->Article->save($this->data)) {
                $this->Session->setFlash('The Article has been saved');
                $this->redirect('/articles/index');
            } else {
                $this->Session->setFlash('Please correct errors below.');
            }
        }
    }

    function edit($id) {
		$this->log("พยายามแก้ไขโดย " . $this->getUsername() , LOG_DEBUG);
        $this->checkAdmin();
        if(empty($this->data)) {
            $this->data = $this->Article->read(null, $id);
        } else {
            $this->cleanUpFields();
            if($this->Article->save($this->data)) {
                $this->Session->setFlash('The Article has been saved');
				$this->log("แก้ไขสำเร็จ " . $this->getUsername() , LOG_DEBUG);
                $this->redirect('/articles/view/' . $id);
            } else {
                $this->Session->setFlash('Please correct errors below.');
            }
        }
    }

	function prepareReservationData($article_id) {		
		return $this->Article->Reservation->findAll("article_id = $article_id");
	}
	
	function isReservedByCurrentUser($article_id) {
		if($this->userId() != null) {
			$user_id = $this->userId();
			$r = $this->Article->Reservation->findAll("article_id = $article_id and user_id = $user_id");
			if($r) {
				return true;
			}
		} 
		return false;
	}

    function view($id) {
		// FIXME: Is $is needed to be validated?
		$this->checkSession();
		$article = $this->Article->read(null, $id);
		
		// FIXME: After fixing view.thtml 
		// $this->data only may be enough
		
		$reservations = $this->prepareReservationData($id);
		
		$this->set('is_reserved_by_this_user', $this->isReservedByCurrentUser($id));
		
        $this->set('article', $article); 

		$this->set('reservations', $reservations);
        $this->data = $article;
    }
	
	function reservation_update($id) {
		$this->checkSession();
		$this->cleanUpFields();
		$user_id = $this->userId();

		if($this->data['Reservation']['cancel'] != "1") {
			$this->data['Reservation']['user_id'] = $user_id;
			$this->data['Reservation']['article_id'] = $id;
			$this->data['Reservation']['expected_submission_date'] =
				$this->data['Reservation']['expected_submission_date_year'] . "-" .
				$this->data['Reservation']['expected_submission_date_month'] . "-" .
				$this->data['Reservation']['expected_submission_date_day'];
	        if($this->Article->Reservation->save($this->data)) {
	            $this->Session->setFlash('จองแปลเรียบร้อยแล้ว');
	        } else {
	            $this->Session->setFlash('พบปัญหาในการจองแปล');
	        }
    	} else {
			if($this->Article->Reservation->delByArticleIdAndUserId($id, $user_id)) {
				$this->Session->setFlash('ยกเลิกจองแปลเรียบร้อยแล้ว');
	        } else {
	            $this->Session->setFlash('พบปัญหาในการยกเลิกการจองแปล');
	        }
		}
		$this->redirect('/articles/view/' . $id);
	}
}
?>
