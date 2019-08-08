let loadComments = (csrfmiddlewaretoken = $('meta[name=csrf]').attr("content")) => {
    let panel = $('#comments');
    $.ajax({
        url: "/user/comments/",
        data: {
            csrfmiddlewaretoken,
        },
        method: 'POST',
        dataType: 'json',
        success: function (data) {
            // console.log(data.comments);
            if(data.success){
                html = '';
                $.each( data.comments, function(key, value) {
                    html += ''+
                    '<a class="dropdown-item d-flex align-items-center" href="#">'+
                        '<div class="font-weight-bold">'+
                            '<div class="text-truncate">'+
                                value.comment+
                            '.</div>'+
                            '<div class="small text-gray-500">'+value.user+' · '+value.date+'</div>'+
                        '</div>'+
                    '</a>';
                });
                panel.html(html);
                if(data.comments.length < 0)
                    $('#items').html(data.comments.length > 5 ? '5+' : data.comments.length)
            }
        },
    });
}

$(document).ready(function(){
    $.ajaxSetup({'cache':false});
    csrfmiddlewaretoken = $('meta[name=csrf]').attr("content");
    loadComments(csrfmiddlewaretoken);
    setInterval(loadComments, 15000);
});