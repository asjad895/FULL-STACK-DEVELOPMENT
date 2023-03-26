// modal.js
function openModal() {
    $('#myModal').modal('show');
}

function getSummary() {
    var text = $('#text').val();
    $.ajax({
        type: 'POST',
        url: '/summary',
        data: {text: text},
        success: function(response) {
            $('#myModal').modal('hide');
            $('#summary').html(response);
        }
    });
}
