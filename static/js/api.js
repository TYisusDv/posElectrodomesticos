var path = window.location.pathname;
var typingTimer;
var CSRFToken = null;
var loadview_loaded = false;
var loadview_retries = 0;
var loaderHTML = `
<div class="d-flex align-items-center justify-content-center mt-3">
    <div class="spinner-border spinner-border spinner-border text-primary" role="status" aria-hidden="true"></div>
    <strong class="ms-2"> Loading...</strong>
</div>
`;

$(document).ready(function () {
    set_pageactive();
    path = window.location.pathname;
    if (api_logged == 0 && path == "/") {
        path = "/auth/sign-in"
    } else if (api_logged == 1 && (path == "/pos" || path == "/pos/")) {
        path = "/pos"
    }
    
    history.pushState(null, null, path);
    loadView();
});

$(document).on("click", "a", function (event) {
    event.preventDefault();

    var pathhref = $(this).attr("href");
    var lv = $(this).attr("lv");

    if (lv == "0") {
        window.location = pathhref;
    } else if(lv=="1"){
        window.open(pathhref, "_blank");
    } else {
        if (pathhref != "javascript:;" && !pathhref.startsWith("#") && pathhref != path) {
            if(loadview_loaded == false){
                path = pathhref;
                history.pushState(null, null, path);
                set_pageactive();
                loadView();
            }
        }
    }
});

$(window).on("popstate", function () {
    if(loadview_loaded == false){
        set_pageactive();
        loadView();
    } else {
        history.pushState(null, null, path);
    }
});

setInterval(function() {
    new AcornIcons().replace();
}, 100);

function api_web_get_tokencsrf(callback) {
    $.ajax({
        url: `/api/web/token/csrf`,
        type: 'GET',
        dataType: 'json',
        success: function (xhr) {
            if (xhr.success) {
                CSRFToken = xhr.token;
                callback(CSRFToken);
            } else {
                CSRFToken = null;
                callback(CSRFToken);
            }
        },
        error: function (xhr) {
            CSRFToken = null;
            callback(CSRFToken);
        }
    });
}

function loadView() {
    if(loadview_loaded == false){
        loadview_loaded = true;
        $('#content').fadeOut(400, function () {
            $(this).html(loaderHTML).fadeIn(400);
        });
        path = window.location.pathname;
        api_web_get_tokencsrf(function (token) {
            if (navigator.onLine) {
                $.ajax({
                    url: `/api/web/view${path}`,
                    type: 'POST',
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                    enctype: 'multipart/form-data',
                    beforeSend: function (xhr, settings) {
                        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                            xhr.setRequestHeader('X-CSRFToken', CSRFToken)
                        }                   
                    },
                    success: function (xhr) {                        
                        $('#content').fadeOut(400, function () {
                            $(this).html(xhr.html).fadeIn(400);
                        });
                        loadview_loaded = false;                        
                    },
                    error: function (xhr) {
                        var html;
                        try {
                            var response = JSON.parse(xhr.responseText);
                            html = response.html;
                            loadview_retries = 0;
                            $('#content').fadeOut(400, function () {
                                $(this).html(html).fadeIn(400);
                            });
                        } catch (error) {
                            if(loadview_retries == 0){
                                loadview_retries++;
                                loadView();
                            }else{
                                loadview_retries = 0;
                                html = "ERROR VIEW";
                                $('#content').fadeOut(400, function () {
                                    $(this).html(html).fadeIn(400);
                                });
                            }                        
                        } 
                        loadview_loaded = false;                  
                    },
                });
            } else {
                $('#content').html('ERROR');
                loadview_loaded = false;
            }
        });
    }
}

function sendDataPost(url, type, formData) {
    return new Promise(function (resolve, reject) {
        api_web_get_tokencsrf(function (token) {
            $.ajax({
                url: `/api/web/${type}/${url}`,
                type: 'POST',
                data: formData,
                dataType: 'json',
                processData: false,
                contentType: false,
                enctype: 'multipart/form-data',
                beforeSend: function (xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                        xhr.setRequestHeader('X-CSRFToken', CSRFToken);
                    }
                },
                success: function (xhr) {
                    resolve(xhr);
                },
                error: function (xhr) {
                    try {
                        var response = JSON.parse(xhr.responseText);
                        reject(response);
                    } catch (error) {
                        var response = {success: false, msg: 'An error occurred.'};
                        reject(response);
                    }
                }
            });
        });
    });
}

function loadNoti(options){
    const {title = '', msg = '', icon = 'cs-error-hexagon', color = 'primary', time = 2000, showProgressbar = false, icon_type = 'class'} = options;
    jQuery.notify({title: title, message: msg, icon: icon}, {type: color, showProgressbar: showProgressbar, delay: time, icon_type: icon_type})
}

function set_pageactive(){
    try{
        $('#menuSide a').removeClass('active');
        $('#menuSide li').removeClass('active');

        $('#menuSide a').each(function() {
            var menuUrl = $(this).attr('href');
            if (menuUrl === path) {
                $(this).addClass('active');
                $(this).closest('li').addClass('active');
            }
        });    
    } catch(e){}
}

function api_showmodal(html) {
    $('#modal-new').html(html);
    $('#modal-new').modal('show');
}