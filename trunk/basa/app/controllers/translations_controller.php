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

 
vendor('/Text/Diff');
vendor('/Text/Diff/Renderer');
vendor('/Text/Diff/Renderer/unified');

class TranslationsController extends AppController
{
    //var $scaffold;
    var $name = 'Translations';
	var $helpers = array('Html', 'Form' , 'Text', 'Javascript');

     function beforeFilter() {
         $this->checkSession();
     }

     function diff($article_id) {
   
         $t1_id = $this->params['form']['t1'];
         $t2_id = $this->params['form']['t2'];

         $t1 = $this->Translation->read(null, $t1_id);
         $t2 = $this->Translation->read(null, $t2_id);


         $b1 = $t1['Translation']['body'];
         $b2 = $t2['Translation']['body'];
         $this->set('t1', $b1);         
         $d = &new Text_Diff(explode("\n", $b1), explode("\n", $b2));
         $r = &new Text_Diff_Renderer_unified();
         $pretty_diff = $r->render($d);

         $this->set('d', $pretty_diff);

         $this->set('article_id', $article_id);
         
     }

	function cancel($article_id) {
    	$a = $this->Translation->Article->read(null, $article_id);
    	$a['Article']['progressive'] = false;
        $this->Translation->Article->save($a);
        $this->redirect('/articles/view/' . $article_id);
	}

    function history($article_id) {
        $this->Translation->recursive = 0;
        $this->set('translations', $this->Translation->findAll("article_id = $article_id" , null, 'revision DESC'));
        $this->set('article_id', $article_id);
    }



    function edit($article_id) {        
        if(empty($this->data)) {
            /* FIXME: Need validator for preventing SQL Injection? */
            $this->data = $this->Translation->find("article_id = " . $article_id, null, 'revision DESC', 1);
            
            $this->data['Translation']['article_id'] = $article_id;
            $this->set('article', $this->Translation->Article->read(null, $article_id));
            $a = $this->Translation->Article->read(null, $article_id);
            $a['Article']['progressive'] = true;
            $this->Translation->Article->save($a);
        } else {
            $this->cleanUpFields();
            $this->data['Translation']['revision']++;
            $this->data['Translation']['user_id'] = $this->getUserId();

            if($this->Translation->save($this->data)) {
                $this->Session->setFlash('The Translation has been saved');

                $a = $this->Translation->Article->read(null, $article_id);
                $a['Article']['progressive'] = false;
                $this->Translation->Article->save($a);
                $this->redirect('/articles/view/' . $this->data['Translation']['article_id']);
            } else {
                $this->Session->setFlash('Please correct errors below.');            
            }
        }
    }
}
?>
