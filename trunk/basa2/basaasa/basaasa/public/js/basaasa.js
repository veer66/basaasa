$(document).ready(function() {
    
	$("#input").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	var old = "";
	function update() {
		
		var t = $("#input").getSelection();
		var url = "http://127.0.0.1/dict/d:" + t.text;

		var callback = function(d) {
            $("#debug").text("arrive");
                all = "";
                
              for(i = 0; i < d.length; i++) {
                      
                    all = all + "\n" +"Dictionary: " +d[i].database + "\n" + d[i].def+ "\n"+ "\n" ;

                  
                }
            
            $("#output").val(all);
		}
    
        if(t.text != "" && t.text != old) { 
            $("#debug").text("start");
            $.get(url , {}, callback, "json");
            old = t.text;
        }
	}
});
