var table_page = 1;
var table_page_previous = table_page;
var table_total_pages = 1;


$(document).on('click', '.prev-link', function () {
    if (table_page > 1) {
        table_page--;
    }
});

$(document).on('click', '.next-link', function () {
    if (table_page < table_total_pages) {
        table_page++;
    }
});

function table_generatepages() {
    var pagination = $('#table-pages');
    pagination.empty();
  
    var startPage = Math.max(1, table_page - 2); // Página de inicio del rango
    var endPage = Math.min(startPage + 4, table_total_pages); // Página final del rango
  
    for (var i = startPage; i <= endPage; i++) {
      var pageLink = $('<a>').addClass('page-link').attr('href', 'javascript:;').text(i);
      var pageItem = $('<li>').addClass('page-item').append(pageLink);
  
      if (i === table_page) {
        pageItem.addClass('active');
      }
  
      pageItem.on('click', function() {
        var clickedPage = parseInt($(this).text(), 10);
        table_page = clickedPage;
      });
  
      pagination.append(pageItem);
    }
  }
  

function table_setdata(id, link, search = '') {
    var formData = new FormData();
    formData.append('search', search);
    formData.append('page', table_page);

    var response = sendDataPost(link, 'data', formData);
    response.then(function (response) {
        if (response.success) {                     
            $(id).html(response.html);
            table_total_pages = response.total_pages;
            if(table_page > table_total_pages){
                table_page = 1;
            }
            table_generatepages();
        } else {
            loadNoti({
                title: 'Error!',
                msg: response.msg,
                color: 'danger'
            });
        }
    }).catch(function (response) {
        loadNoti({
            title: 'Error!',
            msg: response.msg,
            color: 'danger'
        });
    });
}

function table_tempelement(element){
    var $tempElement = $('<div></div>');
    return $tempElement.html(element);
}