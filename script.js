$(document).ready(function () {
  
   $(function() {
                        $('button').click(function() { $.ajax({
                        url: '/process',
                        data: $('form').serialize(),
                        type: 'POST',
                        success: function(response) {
                        console.log('calling initmap')
                        initMap();
                       },
                        error: function(error) {
                        console.log(error);
                       }
                  });
            }); });
});

