function send_data() {
    let features = $('#description').val()
    let quote_icon = "<i class='fas fa-quote-left fa-2x fa-pull-left'></i>"
    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "/",  // Replace with URL of POST handler
        dataType: "json",
        async: true,
        data: JSON.stringify(features),
        success: (result) => {
            for (x in result) {
                $('#hotel_' + x).html(result[x]['hotel']);
                $('#review_' + x).html(quote_icon + result[x]['review']);
            }
            $('#result_div').show();
        },
        error: (result) => {
            alert('There has been an error.');
        }
    })
}