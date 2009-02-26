$(document).ready(function() {
	function build_handler(element) {
		var handler = function() {
			var old = "";
			var update = function() {
				var t = element.getSelection();
				var url = transliterate_service_url;
				//data = {"input": word};
				var params = {};
				params['input'] = t.text;
				
				var callback = function(d) {
		            $("#tubsub").text(d[0]);
				}
		        if(t.text != "" && t.text != old) { 
		            $("#tubsub").text("...");
		            $.post(url , params, callback, "json");
		            old = t.text;
		       }
			}
			element.keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
		}
		return handler;
	}
    $(".source").each(function() {
        build_handler($(this))();
    });
}); 

