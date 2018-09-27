$(document).ready(function () {
  
 $(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $('#loadingImage').show();
        $.ajax({
            type: 'POST',
            url: '/process',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                $('#loadingImage').hide();
                initMap(data);
            },
        });
    });
});
 
});