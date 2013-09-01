/**
 * Defines top position of cut
 */
function definePostion() {
   if (window.location.hash === '#more') {
        // Go to more location
        $('.container').contents().filter(function() {
            return this.nodeType === 8;
        }).replaceWith('<div id="cut" />');
        var cut = $('#cut');
        if (cut.length) {
            var position = cut.position();
            $(document).scrollTop(position.top - 50);
        }
    }
}

/**
 * Deparametrise params
 *
 * @param querystring
 * @returns params
 */
var deparam = function (querystring) {
  // remove any preceding url and split
  querystring = querystring.substring(querystring.indexOf('?')+1).split('&');
  var params = {}, pair, d = decodeURIComponent, i;
  // march and parse
  for (i = querystring.length; i > 0;) {
    pair = querystring[--i].split('=');
    params[d(pair[0])] = d(pair[1]);
  }

  return params;
};

function bindPostCommentHandler() {
    var comment_form = $('#commentbox form');

    comment_form.submit(function(e) {
        e.preventDefault();
        var postData = $(this).serialize();

        $.ajax({
            type: 'post',
            url: $(this).attr('action'),
            data: postData,
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
                var comments_number = parseInt($('span.glyphicon-comment').parent().text());
                var update_comments_number = comments_number + 1;
                var comment_data = deparam(postData);
                var panel = '<div id="new_comment" class="panel panel-info">';
                var panel_header = '<div class="panel-heading"><strong>' +
                    comment_data.name.replace(/\+/g, ' ') + '</strong> said:' + '</div>';
                var panel_body = '<div class="panel-body">' +
                    comment_data.comment.replace(/\+/g, ' ') + '</div>';
                // hide form
                comment_form.hide();
                // hide no comments
                $('#nocomments').hide();
                panel = panel + panel_header + panel_body + '</div>';
                $(panel).insertBefore('#comments .panel:first');
                $('#new_comment').fadeIn();
                $('#new_comment').focus();
                $(document).scrollTop($(document).scrollTop() - 50);
                $('.alert').append('<p>Thank you for your comment.</p>');
                // update comments count
                $('span.glyphicon-comment').parent().fadeIn();
                $('span.glyphicon-comment').parent().html(
                       '<span class="glyphicon glyphicon-comment" style="padding-right: 10px;"></span>' +
                           update_comments_number);
                $('.alert').show();

                // hide alert
                setTimeout(function() {
                    $('.alert').fadeOut();
                }, 3000);
                bindPostCommentHandler();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                comment_form.replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');
            }
        });
    })
}

$(document).ready(function () {
    definePostion();
    bindPostCommentHandler();
    // Scroll to top
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });
    $('.scrollup').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
})