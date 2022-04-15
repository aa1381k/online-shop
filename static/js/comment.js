function sendcomment(article_id){
    var comment = $('#commenttext').val();
    var parent_id = $('#parentid').val();
    $.get('/articles/article-comment/',{
        comment : comment,
        article_id : article_id,
        parent_id : parent_id,
    }).then(res=>{
        console.log(res);
        $('#comments_area').html(res);
    });
}

function comment_anwser(comment_id){
    $('#parentid').val(comment_id);
    document.getElementById('comment_form').scrollIntoView({behavior:"smooth"});
}