<?php
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


class ArticlesController extends AppController
{
    
	//var $scaffold;
	var $name = 'Articles';
	var $helpers = array('Html', 'Form' , 'Text', 'Javascript');

    function index() {
		
        $this->Article->recursive = 0;
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
        $this->checkAdmin();
        if(empty($this->data)) {
            $this->data = $this->Article->read(null, $id);
        } else {
            $this->cleanUpFields();
            if($this->Article->save($this->data)) {
                $this->Session->setFlash('The Article has been saved');
                $this->redirect('/articles/view/' . $id);
            } else {
                $this->Session->setFlash('Please correct errors below.');
            }
        }
    }

    function view($id) {
		$this->checkSession();
        $this->set('article', $this->Article->read(null, $id));
        $this->data = $this->Article->read(null, $id);
    }

}
?>
