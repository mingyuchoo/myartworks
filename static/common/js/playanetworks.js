/*
 * Setup csrf token to use
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


/*
 * ImageField
 */
$(document).ready(function(){
   var fileTarget = $('.filebox .upload-hidden');
    fileTarget.on('change', function(){
        if(window.FileReader){
            // 파일명 추출
            var filename = $(this)[0].files[0].name;
        } else {
            // Old IE 파일명 추출
            var filename = $(this).val().split('/').pop().split('\\').pop();
        };
        $(this).siblings('.upload-name').val(filename);
    });
    //preview image
    var imgTarget = $('.preview-image .upload-hidden');

    imgTarget.on('change', function(){
        var parent = $(this).parent();
        parent.children('.upload-display').remove();

        if(window.FileReader){
            //image 파일만
            if (!$(this)[0].files[0].type.match(/image\//)) return;
            var reader = new FileReader();
            reader.onload = function(e){
                var src = e.target.result;
                parent.append('<div class="upload-display"><div class="upload-thumb-wrap"><img src="'+src+'" class="upload-thumb"></div></div>');
            }
            reader.readAsDataURL($(this)[0].files[0]);
        } else {
            $(this)[0].select();
            $(this)[0].blur();
            var imgSrc = document.selection.createRange().text;
            parent.append('<div class="upload-display"><div class="upload-thumb-wrap"><img class="upload-thumb"></div></div>');
            var img = $(this).siblings('.upload-display').find('img');
            img[0].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enable='true',sizingMethod='scale',src=\""+imgSrc+"\")";
        }
    });
});

