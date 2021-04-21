
$(document).ready(function(){

$("#addToCart").on('click',function(){
var product_id = $("#addToCart").attr("product_id")

var product_quantity = $('#product_quantity').val()

$.ajax({
			url: '/product/addToCart/',
			data:{
            "product_id":product_id,
            "product_quantity":product_quantity

            },
			dataType:'json',
			// beforeSend:function(){
			// 	$(".ajaxLoader").show();
			// },
			success:function(res){
				
                $("#addToCart").hide();

				$("#filteredProducts").html(res.data);

				$("#filteredProducts").html(res.data);
				alert("Added To Cart Successfully!")


				
			},
            error: function (response) {
                console.error("This is an error");
            }
		});


});

//productTotal Price for Cart Page

   var loadingTimePrice = $(".total_price")
    var initial_total_price_holder = []

   for(i=0;i<loadingTimePrice.length;i++){
       var currentUnitTOtalPrice = $("#"+(i+1)).text()
       currentUnitTOtalPrice = currentUnitTOtalPrice.split(" $")


       initial_total_price_holder.push(currentUnitTOtalPrice)

   }

var convertedSubtotalPriceArray = []
  for(let x=0; x<initial_total_price_holder.length; x++){

      let convertedSubtotalPrice = initial_total_price_holder[x].toString()
      convertedSubtotalPrice = convertedSubtotalPrice.replace("$","");

      convertedSubtotalPriceArray.push(convertedSubtotalPrice)
  }


  var subtotal_price = convertedSubtotalPriceArray.reduce((a,b)=>parseInt(a)+parseInt(b))

  $("#subTotal").text("$"+subtotal_price);


  var taxes = ((subtotal_price *5)/ 100);

  $("#taxes").text(taxes);

  $("#allTotal").text(subtotal_price+taxes);


   $("#productQuantity input").on('change',function() {

       var product_quantity_array = []

      var allProducts = $(".product_price");

      for(i=0;i<allProducts.length;i++){

          var each_product_quantity =  $(allProducts[i]).val()
          product_quantity_array.push(each_product_quantity);


      }


       var product_price_holder = []
       var product_price = $("#productMainDIv #productPrice").text()
       product_price = product_price.split("x $");


       var total_price_holder = []

       for(i=0;i<allProducts.length;i++){



           var totalCalculatedPrice = (product_quantity_array[i]*product_price[i+1]);

           total_price_holder.push(totalCalculatedPrice);
            $("#"+(i+1)).text("$"+totalCalculatedPrice+'.0');

       }

       var subTotalPrice = total_price_holder.reduce((a, b) => a + b, 0)

       $("#subTotal").text("$ "+subTotalPrice);
       console.log("Subtotal: "+subTotalPrice);


       //Percentage Calculation

       var taxes = ((subTotalPrice *5)/ 100);
       $("#taxes").text(taxes);

       //All Total Price Calculation



       $("#allTotal").text(subTotalPrice+taxes);



  });

});