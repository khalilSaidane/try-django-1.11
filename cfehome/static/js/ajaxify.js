function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb)
    btn.attr("count", newCount)
}

$(document).ready(function () {
    // Ajaxifying follow button
    $('.btn-follow').click(function (e) {
        e.preventDefault();
        var this_ = $(this);
        var followUrl = this_.attr('href');
        var followersCount = parseInt(this_.attr('count'));
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

    // Ajaxifying fol like
    $('.btn-like').click(function (e) {
        e.preventDefault();
        var this_ = $(this);
        var likeUrl = this_.attr('href');
        var likeCount = parseInt(this_.attr('count'));
        $.ajax({
            url: likeUrl,
            method: 'GET',
            data: {},
            success: function (data) {
                if (data.liked) {
                    console.log(likeCount)
                    likeCount += 1;
                    updateText(this_, likeCount, "Unlike");
                } else {
                    likeCount -= 1;
                    updateText(this_, likeCount, "Like")
                }
            }, error: function (error) {
                console.log('error');
                console.log(error)
            }
        });
    });
});