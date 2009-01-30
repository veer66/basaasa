$(document).ready(function() {
	var t = $("#body").val();

		var url = "http://127.0.0.1/vee/segment.php";
		var params = {};
		params['text'] = t;
		params['lang'] = 'lang';
		var callback = function(d) {
			all = "";
            for(i = 0; i < d.length; i++) {
    
                all = all+d[i]+"\n";
            	//$("#segment").val(d[i].database);
              
            }
        
       $("#segment").val(all);
	}

            $.post(url ,params, callback, "json");

	
}); 

