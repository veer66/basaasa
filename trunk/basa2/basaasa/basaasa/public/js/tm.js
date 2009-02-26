$(document).ready(function() {	
	function build_handler(element) {
        var handler = function() {
            $("#tm").text("...");
            var old = "";
            
            var update = function() {
                var t = $(element).getSelection();
                if(t.text != "" && t.text != old) {
                    var doc_id = $("#doc_id").val();
                    var url = tm_service_url;	

                    var callback = function(data) {				
                        output = "";
                        for(i=0; i < data.length;i++) {
                            output = output + data[i][0] +  
                                     "\n" + data[i][1] + "\n" + 
                                     data[i][2] * 100 + "%\n\n";
                        }
                        $("#tm").text(output);
                    }

                    var params = {"fragment": t.text};

                    $.post(url, params, callback, "json");
                    old = t.text;
                }
            }
            element.keydown(update).keyup(update).mousedown(update).mouseup(update).mousemove(update)
        }
        return handler;
    }

    $(".source").each(function() {
        build_handler($(this))();
    });
}); 
