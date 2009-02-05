$(document).ready(function() {
	function build_handler(query) {
		var handler = function() {
			var old = "";
			var update = function() {
				var t = $(query).getSelection();
				var url = transliterate_service_url;
				//data = {"input": word};
				var params = {};
				params['input'] = t.text;
				
				var callback = function(d) {
		    
		            $("#tubsub").val(d);
				}
		        if(t.text != "" && t.text != old) { 
		            $.post(url , params, callback, "json");
		            old = t.text;
		       }
			}
			$(query).keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
		}
		return handler;
	}
	build_handler("#segment")();
	build_handler("#body")();
	build_handler("#title")();
	build_handler("#source_title")();
}); 

