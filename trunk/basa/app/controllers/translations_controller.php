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
