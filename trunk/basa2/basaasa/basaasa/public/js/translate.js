$(document).ready(function() {		
	var t = $("#segment").val();
	var segments = t.replace(/\r+/, "").split(/\n\s*\n+/);	
	var url = translate_service_url;
	var params = {"source": segments.toSource()};
	var callback = function(data) {
		var body = [];
		for(i = 0; i < segments.length; i++) {
			body.push(segments[i] + "\n" + data[i]);
		}
		alert("!!!: " + body.toSource());
		$("#body").val(body.join("\n\n"));
	}
	$.post(url, params, callback, "json");
}); 
