$('#comment-form').on('submit', function(event) {
        event.preventDefault();
        console.log('Submitted');
        console.log($('#id_body').val());
        write_comment();
    });

function write_comment () {
    console.log('write_post function started!');
    $.ajax({
        url : '/blog/read/' + $("#post_id").val(),
        type : 'POST',
        data : { com_body: $('#id_body').val() },
        headers : {'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()},

        success : function(json) {
            $('#id_body').val(''),
            console.log(json)
        },

        error : function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText)
        },
    });
}