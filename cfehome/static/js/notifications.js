$(document).ready(function () {
    // Ajaxifying follow button
    $('.notification').click(function (e) {
        var this_ = $(this);
        var readNotificationUrl = this_.attr('read-url');
        $.ajax({
            url: readNotificationUrl,
            method: 'PUT',
            data: {},
            success: function (data) {
              console.log('success')
            }, error: function (error) {
                console.log('error');
                console.log(error)
            }
        });
    });
});