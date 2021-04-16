$(document).ready(function(){
           
    
    $("#filter_brand").on('click',function(){

        var _filterObj={};
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
            
			var _filterKey=$(this).data('filter');
            console.log(_filterKey)
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});

        var url = window.location.pathname;
        var _catId = url.substring(url.lastIndexOf('/') + 1);
        _filterObj.catId=_catId;

        $.ajax({
			url: '/product/brandbasedproduct/',
			data:_filterObj,
			dataType:'json',
			
			success:function(res){
				console.log(res);
				$("#filteredProducts").html(res.data);
				//$(".ajaxLoader").hide();
			}
		});

    });

        
    });