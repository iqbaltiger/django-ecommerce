$(document).ready(function(){
        $('input[type="checkbox"]').click(function(){
            if($(this).prop("checked") == true){
                // $("#result").html("Checkbox is checked.");
                var brandId = $(this).attr("id");
               
                $.ajax({
                    url: '/product/brandbasedproduct/',
                    data: {
                    'brand': brandId
                    },
                    dataType: 'json',
                    success: function (data) {
                    if (data) {
                        alert(data);
                    }
                    }
                });
            }
            
        });


        alert("Category Page")
    });