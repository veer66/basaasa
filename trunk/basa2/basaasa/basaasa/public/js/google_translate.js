$(document).ready(function() {
	google.language.getBranding('branding');
});

function translate_with_elements(source_element, target_element) {
    var source_val = source_element.val();
    google.language.detect(source_val, function(result) {
      if (!result.error && result.language) {
        google.language.translate(source_val, result.language, "th",
           function(result) {               
               if (result.translation) {            	   
            	   var translated_text = result.translation;            	   
                   target_element.val(translated_text);
               }
           });
      }
    });
}

function translate(source, target) {
    source_element = $(source);
    target_element = $(target);
    translate_with_elements(source_element, target_element);
}
