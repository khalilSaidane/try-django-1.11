function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb)
    btn.attr("data-followers", newCount)
}

$(document).ready(function () {
    $('.btn-follow').click(function (e) {
        e.preventDefault();
        var this_ = $(this);
        var followUrl = this_.attr('href');
        var followersCount = parseInt(this_.attr('data-followers'));
        $.ajax({
            url: followUrl,
            method: 'GET',
            data: {},
            success: function (data) {
                if (data.is_following) {
                    console.log(followersCount)
                    followersCount += 1;
                    updateText(this_, followersCount, "Unfollow");
                } else {
                    followersCount -= 1;
                    updateText(this_, followersCount, "Follow")
                }
            }, error: function (error) {
                console.log('error');
                console.log(error)
            }
        });
    });
});