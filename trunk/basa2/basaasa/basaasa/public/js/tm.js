$(document).ready(function() {	
	$("#body").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	var old = "";
	
	function update() {
		var t = $("#body").getSelection();
		if(t.text != "" && t.text != old) {
			var doc_id = $("#doc_id").val();
			var url = tm_service_url;	
			var callback = function(data) {				
				output = "";
				for(i=0; i < data.length;i++) {
					output = output + data[i][0] + ":" +  data[i][1] + ":" 
							 + data[i][2] * 100 + "%\n";
				}
				$("#tm").val(output);
			}
			var params = {"fragment": t.text};
	        $.post(url, params, callback, "json");
	    	old = t.text;
	    }
	}
      
}); 