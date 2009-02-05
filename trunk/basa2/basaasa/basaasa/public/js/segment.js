$(document).ready(function() {
	var t = $("#body").val();
	var url = segment_service_url;
	var params = {};
	params['text'] = t;
	params['lang'] = 'lang';
	var callback = function(d) {
		all = "";
	    for(i = 0; i < d.length-1; i++) {
	    	all = all+d[i]+"\n\n";
	    }
	    all = all.substring(0,all.length-2);
	    $("#segment").val(all);
	}
    $.post(url ,params, callback, "json");
}); 

