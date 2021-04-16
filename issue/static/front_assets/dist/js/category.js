$(document).ready(function(){
       
        $('input[type="checkbox"]').click(function(){
            if($(this).prop("checked") == true){
                // $("#result").html("Checkbox is checked.");
                var brandId = $(this).attr("id");
                //$("#filteredProducts").hide();
                
               
                $.ajax({
                    url: '/product/brandbasedproduct/',
                    data: {
                    'brand': brandId
                    },
                    dataType: 'json',
                   success:function(res){
                    console.log(res);
                    
                    $("#filteredProducts").html(res.data);
                    // $(".ajaxLoader").hide();
			      }



                });
            }
            
        });


        
    });