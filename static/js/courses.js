$(document).ready(function() {
    $(".class_is_done").on("change", function () {
        var pk = $(this).closest('tr').attr("data-pk"); // select the correct row
        var is_done = $(this).is(':checked') ? 1 : 0;
        if (typeof is_done === "undefined") {
            is_done = 0;
        }
        var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({
            type: "POST",
            url: "update_status/",
            data: { 
                pk: pk, 
                is_done: is_done,
                csrfmiddlewaretoken: csrf_token
            },
            dataType: "json",
            success: function (data) {
                console.log("Success:", data);
                console.log("id_done",is_done);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });
});



