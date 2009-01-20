$(document).ready(function() {
		
		
	
		var t = $("#segment").val();
		//alert(t);
		var myArray=t.split("\n\n");	
		var url = "http://127.0.0.1/mt";
		var all = [];
		//alert(myArray.length);
		for(i = 0; i < myArray.length; i++) {
			var params = {};
			params['source'] = myArray[i];
			params['format'] = "text";

			callback = function(j) {
//				alert(i);

//				all.push([i,j]);
				//var Array=myArray.split("\n");
//                all.sort();
//                alert(all);
            	//$("#segment").val(d[i].database);
              
			}
//			$.post(url ,params, callback, "text");
			s = {"type": "POST", 
				 "url": url, 
				 "data": params, 
//				 "global": false,
				 "async": false,
				 "success": function(data) {
								$("#body").val($("#body").val() + "\n\n" + myArray[i]+"\n"+data);
							}
			};			
			$.ajax(s);	
		}
		//$("#body").val(all);
}); 