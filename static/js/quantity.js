$(document).ready(function () {
    $('.increment-btn').click(function (e) {
        e.preventDefault();
        var incre_value = $(this).parents('.quantity').find('.qty-input').val();
        var max_value = $(this).parents('.quantity').find('.max-quantity').val();
        var value = parseInt(incre_value, 10);
        value = isNaN(value) ? 0 : value;
        if(value < parseInt(max_value)) {
            // Increment Value by 1
            value++;

            // Update Incremented value
            $(this).parents('.quantity').find('.qty-input').val(value);

            // Update API
            var product_id=$(this).closest('.product_data').find(".prod_id").val();
            var product_qty=$(this).closest('.product_data').find(".qty-input").val();
            var token=$('input[name=csrfmiddlewaretoken]').val();
    
            $.ajax({
                method:"POST",
                url:"/update-cart",
                data:{
                    'product_id':product_id,
                    'product_qty':product_qty,
                    csrfmiddlewaretoken:token
                },
            
                success:function(response){
                    alertify.success(response.status)
                }
            });    
        } else {
            alertify.error("Max Limit")
        }

    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();
        var decre_value = $(this).parents('.quantity').find('.qty-input').val();
        var value = parseInt(decre_value, 10);
        value = isNaN(value) ? 0 : value;
        if(value>1){
            // Decrement value by 1
            value--;

            // Update Text Field
            $(this).parents('.quantity').find('.qty-input').val(value);

            // Update API
            var product_id=$(this).closest('.product_data').find(".prod_id").val();
            var product_qty=$(this).closest('.product_data').find(".qty-input").val();
            var token=$('input[name=csrfmiddlewaretoken]').val();
    
            $.ajax({
                method:"POST",
                url:"/update-cart",
                data:{
                    'product_id':product_id,
                    'product_qty':product_qty,
                    csrfmiddlewaretoken:token
                },
            
                success:function(response){
                    alertify.success(response.status)
                }
            }); 
        } else {
            alertify.error("Min Limit")
        }
    });

    $('.addToCartBtn').click(function(e){
        e.preventDefault();

        var product_id=$(this).closest('.product_data').find(".prod_id").val();
        var product_qty=$(this).closest('.product_data').find(".qty-input").val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method:"POST",
            url:"/add-to-cart",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken:token
            },
        
            success:function(response){
                console.log(response)
                alertify.success(response.status)

            }
            
        });
    });

    // $('.changeQuantity').click(function(e){
        // e.preventDefault();

    //     var product_id=$(this).closest('.product_data').find(".prod_id").val();
    //     var product_qty=$(this).closest('.product_data').find(".qty-input").val();
    //     var token=$('input[name=csrfmiddlewaretoken]').val();

    //     $.ajax({
    //         method:"POST",
    //         url:"/update-cart",
    //         data:{
    //             'product_id':product_id,
    //             'product_qty':product_qty,
    //             csrfmiddlewaretoken:token
    //         },
        
    //         success:function(response){
    //             alertify.success(response.status)

    //         }
            
    //     });
    // });


    $('.delete-cart-item').click(function(e){
        e.preventDefault();

        var product_id=$(this).closest('.product_data').find(".prod_id").val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method:"POST",
            url:"delete-cart-item",
            data:{
                'product_id':product_id,
                csrfmiddlewaretoken:token
            },
        
            success:function(response){
                alertify.success(response.status)
                $('.cartdata').load(location.href + " .cartdata")

            } 

        });   

    });
});