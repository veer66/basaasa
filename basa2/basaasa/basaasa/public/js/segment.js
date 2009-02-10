$(document).ready(function() {
	var t = $("#body").val();
	var url = segment_service_url;
	var params = {};
	params['text'] = t;
	params['lang'] = 'eng';
	var callback = function(sentences) {
	    $("#segment").val(sentences.join("\n\n"));
	}
    $.post(url ,params, callback, "json");
}); 

