$(document).ready(function() {
	$(".textunit").click(function() {
		tu_id = parseInt(/^tu(.+)$/g.exec($(this).attr('id'))[1]);
		
	});
});