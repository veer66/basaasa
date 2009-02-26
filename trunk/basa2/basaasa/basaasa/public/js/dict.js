$(document).ready(function() {
	function build_handler(element) {
		var handler = function() {
			var old = "";
			var update = function() {
				var t = element.getSelection();
				var url = dict_service_url;
				var callback = function(d) {
					all = "";
		            for(i = 0; i < d.length; i++) {
		            	all = all + "\n" +"Dictionary: " +d[i].database + "\n" + d[i].def+ "\n"+ "\n" ;	              
		            }	            
		            $("#dictionary").text(all);
				}	    
		        if(t.text != "" && t.text != old) { 
		            $("#dictionary").text("...");
		            $.get(url , {word: t.text}, callback, "json");
		            old = t.text;
		        }
			}
			element.keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update);
		}	
		return handler;
	}
	$(".source").each(function() { build_handler($(this))(); });
}); 
