function add_cart_count(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/addcount/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {

            cart_count()
        },
        error: function (data) {
            alert('请求失败3')
        }


    })
}

function sub_cart_count(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/subcount/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {

            cart_count()
        },
        error: function (data) {
            alert('请求失败2')
        }
    })
}


function cart_count() {

    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var total_price = 0;
    $.ajax({
        url: '/carts/count/',
        type: 'GET',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},

        success: function (data) {
            if (data.code == '200') {
                for (i = 0; i < data.goods_list.length; i++) {
                    $('.num_show_' + data.goods_list[i]['id']).val(data.goods_list[i]['count']);
                    $('#xiaoji_' + data.goods_list[i]['id']).html(data.goods_list[i]['total'] + '元');
                    total_price +=  parseFloat(data.goods_list[i]['total']);
                    $('#total_price').html(total_price)
                }


            }
        },
        error: function (data) {

        }
    })
}

cart_count();

function del_cart_goods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/delcartgoods/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == '200'){
                cart_count();
                location.reload()
            }
        },
        error: function (data) {
            alert('请求失败')
        }


    })
}