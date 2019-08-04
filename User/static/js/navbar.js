let loadComments = (csrfmiddlewaretoken) => {
    let panel = $('#comments');
    $.ajax({
        url: "/user/comments/",
        data: {
            csrfmiddlewaretoken,
        },
        method: 'POST',
        dataType: 'json',
        success: function (data) {
            console.log(data);
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
                panel.after(html);
            }
        },
    });
}

$(document).ready(function(){
    csrfmiddlewaretoken = $('meta[name=csrf]').attr("content");
    loadComments(csrfmiddlewaretoken);
    setInterval(loadComments(csrfmiddlewaretoken), 5000);
});