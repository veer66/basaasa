$(document).ready(function() {		
	
		var t = $("#segment").val();
		var myArray=t.split("\n\n");	
		var url = "http://127.0.0.1/mt";
		var all = [];
		for(i = 0; i < myArray.length; i++) {
			var params = {};
			params['source'] = myArray[i];
			params['format'] = "text";

			callback = function(j) {

			}

			s = {"type": "POST", 
				 "url": url, 
				 "data": params, 
//				 "global": false,
				 "async": false,
				 "success": function(data) {
				
			$("#body").val($("#body").val()+ myArray[i]+"\n"+data+"\n\n");
							}
			};			
			$.ajax(s);	
		}
}); 


$(document).ready(function() {		
	
	var t = $("#source_title").val();
	var myArray=t.split("\n\n");	
	var url = "http://127.0.0.1/mt";
	var all = [];
	for(i = 0; i < myArray.length; i++) {
		var params = {};
		params['source'] = myArray[i];
		params['format'] = "text";

		callback = function(j) {

		}

		s = {"type": "POST", 
			 "url": url, 
			 "data": params, 
//			 "global": false,
			 "async": false,
			 "success": function(data) {
			
		$("#title").val($("#title").val()+data);
						}
		};			
		$.ajax(s);	
	}
}); 