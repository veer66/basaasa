<?php
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
				$this->Session->setFlash('Please correct errors below.');
				$this->set('articleArray', $this->Comment->Article->generateList());
				$this->set('userArray', $this->Comment->User->generateList());
			}
		}
	}

}
?>