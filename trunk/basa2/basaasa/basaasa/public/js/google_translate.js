$(document).ready(function() {
	
	function newline_to_br(txt) {
        return txt.replace(/\n\n+/g, "<br/>");
    }
	
	function remove_return(txt) {
		return txt.replace("/\r/g", "");
	}
	
	function filter_empty(a) {
		return jQuery.grep(a, function (tok) { return tok != ""; });
	}
	
	var text = remove_return($("#segment").val());
	var text_for_google = newline_to_br(text);
	var source_fragments = filter_empty(text.split(/\n\n+/));
    google.language.detect(text_for_google, function(result) {
      if (!result.error && result.language) {
        google.language.translate(text_for_google, result.language, "th",
           function(result) {               
               if (result.translation) {            	   
            	   var translated_text = result.translation;            	   
            	   var target_fragments = filter_empty(translated_text.split("<br/>"));
            	   var fragments = [];
            	   for(i = 0; i < source_fragments.length; i++) {
            		   fragment = source_fragments[i] + "\n" + target_fragments[i];
            		   fragments.push(fragment);
            	   }
               }
               $("#body").val(fragments.join("\n\n"));
           });
      }
    });
});