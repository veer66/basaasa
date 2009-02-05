$(document).ready(function() {
	function build_handler(query) {
		var handler = function() {
			var old = "";
			var update = function() {
				var t = $(query).getSelection();
				var url = dict_service_url;
				var callback = function(d) {
					all = "";
		            for(i = 0; i < d.length; i++) {
		            	all = all + "\n" +"Dictionary: " +d[i].database + "\n" + d[i].def+ "\n"+ "\n" ;	              
		            }	            
		            $("#dictionary").val(all);
				}	    
		        if(t.text != "" && t.text != old) { 
		            $.get(url , {word: t.text}, callback, "json");
		            old = t.text;
		        }
			}
			$(query).keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update);
		}	
		return handler;
	}
	build_handler("#segment")();
	build_handler("#body")();
	build_handler("#title")();
	build_handler("#source_title")();
}); 
