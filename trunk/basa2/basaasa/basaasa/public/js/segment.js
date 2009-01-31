$(document).ready(function() {
	var t = $("#body").val();

		var url = "http://127.0.0.1/vee/segment.php";
		var params = {};
		params['text'] = t;
		params['lang'] = 'lang';
		var callback = function(d) {
			all = "";
            for(i = 0; i < d.length-1; i++) {
    
                all = all+d[i]+"\n\n";
                
            	//$("#segment").val(d[i].database);
              
            }
           all = all.substring(0,all.length-2);
            //alert(all.substring(0,all.length-1));
                       
       $("#segment").val(all);
	}

            $.post(url ,params, callback, "json");

	
}); 

