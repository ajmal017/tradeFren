$(function () {
    $('button').click(function () {
        var recipient = $('#recipient_address').val();
        $.ajax({
            url: '/create_tx_func',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});