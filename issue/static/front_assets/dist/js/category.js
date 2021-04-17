$(document).ready(function(){

    
           
    $(".ajaxLoader").hide();
    $("#filter_brand").on('click',function(){
    var _filterObj={};
    var url = window.location.pathname;
    var _catId = url.substring(url.lastIndexOf('/') + 1);
    _filterObj.catId=_catId;

        
    $(".filter-checkbox").each(function(index,ele){
        var _filterVal= $(this).val();
        
        var _filterKey= $(this).data('filter');
        // chosen_list = $(this).nextSibling.innerText
        // $(".filter-summary-filterList").append(chosen_list);
        


        console.log(_filterKey)
        _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
            return el.value;
        });
    });

        
        
        $.ajax({
			url: '/product/brandbasedproduct/',
			data:_filterObj,
			dataType:'json',
			// beforeSend:function(){
			// 	$(".ajaxLoader").show();
			// },
			success:function(res){
				console.log(res);
				$("#filteredProducts").html(res.data);
				//$(".ajaxLoader").hide();
			}
		});

    });

    
    //Sorting Order
    $('#sorting_order').on('change', function() {
       
        // var sorting_action = {};
        // sorting_action.sort_value = this.value
        var url = window.location.pathname;
       var _catId = url.substring(url.lastIndexOf('/') + 1);
        // sorting_action.catId=_catId;
       alert(this.value) 

        $.ajax({
			url: '/product/sortingproduct/',
			data:{

                'sort_order_value':this.value,
                'catId':_catId
            },
			dataType:'json',
			// beforeSend:function(){
			// 	$(".ajaxLoader").show();
			// },
			success:function(res){
				console.log(res);
				$("#filteredProducts").html(res.data);
				//$(".ajaxLoader").hide();
			}
		});

     

    });
    //End Sorting Order

        
    });