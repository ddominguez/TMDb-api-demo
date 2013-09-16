$(function() {
    $('#cast-list li a').click(function(event) {
        event.preventDefault();
        url = $(this).data('url');

        $.ajax({
            url: url,
            type: 'GET'
        })
        .done(function(data) {
            $('body').append('<div class="modal-back">'+data+'</div>');
        });
    });

    $('body').on('click', 'div.modal-back', function() {
        $(this).remove();
    });
});