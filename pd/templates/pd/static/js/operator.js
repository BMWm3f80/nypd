// var csrftoken = $.cookie('csrftoken');
//
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
//
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });








$('.comp').click(function(event) {
      // You gotta include the csrf_token in your post data
    id=$(this).attr("job-id");
    alert("Is the order printed already with ID:"+id+"?")
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'update',
        data: {'id': id},
        success: function (data, textStatus) {
           location.reload();
        },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });
  });
