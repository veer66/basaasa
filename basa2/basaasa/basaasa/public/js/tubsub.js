$(document).ready(function() {
	
	$("#segment").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	
	var old = "";
	function update() {
		
		var t = $("#segment").getSelection();
		var url = "http://127.0.0.1/vee/tubsube2t";
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

$(document).ready(function() {
	
	$("#source_title").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	
	var old = "";
	function update() {
		
		var t = $("#source_title").getSelection();
		var url = "http://127.0.0.1/vee/tubsube2t";
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

$(document).ready(function() {
	
	$("#title").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	
	var old = "";
	function update() {
		
		var t = $("#title").getSelection();
		var url = "http://127.0.0.1/vee/tubsube2t";
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

$(document).ready(function() {
	
	$("#body").keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
	
	var old = "";
	function update() {
		
		var t = $("#body").getSelection();
		var url = "http://127.0.0.1/vee/tubsube2t";
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

