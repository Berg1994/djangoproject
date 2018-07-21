function goods_add(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/addtocart/',
        data: {'goods_id': id},
        type: 'POST',
        headers: {'X-CSRFToken': csrf},
        dataType: 'json',
        success: function (data) {
            if (data.code == '200') {
                $('#goods_' + id).html(data.c_num)
                get_count_price()
            }
        },
        error: function (data) {
            alert('请求失败')

        }
    });
}

function goods_sub(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/subtocart/',
        type: 'POST',
        dataType: 'json',
        data: {'goods_id': id},
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code == '200') {
                $('#goods_' + id).html(data.c_num)

                if (data.c_num == '0') {
                    $('#cart_to_del_' + id).remove()
                }
                get_count_price()
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    });
}


$(function () {
    $.get('/axf/goodsnum/', function (data) {

        if (data.code == '200') {
            for (i = 1; i < data.carts.length; i++) {
                $('#goods_' + data.carts[i].goods_id).html(data.carts[i].c_num)
            }
        }
    })
});

function change_cart_status(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/changecartstatus/',
        data: {'cart_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code == '200') {
                if (data.cart_status) {
                    s = '√'
                } else {
                    s = 'x'
                }
                $('#cart_status_' + id).html(s)
                get_count_price()
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    })
}

function get_count_price() {
    $.get('/axf/goodscount/', function (data) {
        if (data.code == '200') {
            $('#all_price').html('总价：' + data.count)
        }
    });
}

get_count_price();

function order() {

}


function make_order(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
       url:'/axf/makeorder/',
       dataType:'json',
       headers:{'X-CSRFToken':csrf },
        type:'POST',
        success:function (data) {
           if(data.code == '200'){
               location.href= '/axf/getorder?order_id=' + data.order_id
           }
        },
        error:function (data) {
            alert('请求失败')
        }
    });
}




function changeorderstatus(id) {
    var csrf= $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
       url:'/axf/changeorderstatus/',
       data:{'order_id':id},
       dataType:'json',
        type:'POST',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if(data.code == '200'){
                location.href = '/user/mine/'
            }
        },
        error:function (data) {
            alert('请求失败')
        }
    });
}