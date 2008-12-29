$(document).ready(function() {
	
	$("#source_body").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	
	var old = "";
	function update() {
		
		var t = $("#source_body").getSelection();
		var url = "http://127.0.0.1/vee/tubsube2t.php";
		//data = {"input": word};
		var params = {};
		params['input'] = t.text;
		
		var callback = function(d) {
    
            $("#tubsub").val(d);
		}
    
        if(t.text != "" && t.text != old) { 
            //$("#debug").text("start");
            $.post(url , params, callback, "json");
            old = t.text;
       }
	}
}); 