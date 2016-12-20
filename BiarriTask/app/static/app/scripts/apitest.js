$(document).ready(function () {
    JuliusCaesar = { name: 'Julius Caesar', author: 'William Shakespeare' }
    $('#postBtn').click(function () {
        button = $(this);
        button.addClass('btn-warning');
        $.post('/plays/', JuliusCaesar, function (data, status) {
            console.log(data)
            console.log(status)
            button.removeClass('btn-warning');
            if (status == 'success') {
                button.addClass('btn-success');
            }
            else {
                button.addClass('btn-danger');
            }
        });
    });
});