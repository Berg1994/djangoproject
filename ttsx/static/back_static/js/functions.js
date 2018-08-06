function add_count(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/goods/addcount/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {

            count()
        },
        error: function (data) {
            alert('请求失败3')
        }


    })
}

function sub_count(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/goods/subcount/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {

            count()
        },
        error: function (data) {
            alert('请求失败2')
        }
    })
}


function count() {

    var id = (location.search).split('=')[1];
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/goods/count/',
        data: {'id': id},
        type: 'GET',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code == '200') {
                $('#show_count').html(data.cart_count);
                $('.num_show').val(data.count);
                $('#total_price').html(data.total_price);
                $('')
            }
        },
        error: function (data) {
            alert(222)
        }
    })
}

count();

function add_to_cart(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/goods/addtocart/',
        data: {'goods_id': id},
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            count();
        },
        error: function (data) {
            alert('请求失败1')
        }

    })
}

function f() {

}

function add_cart_count(id) {
    alert(222)
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
    alert(111)
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

    var id = (location.search).split('=')[1];
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/count/',
        data: {'id': id},
        type: 'GET',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code == '200') {
                $('#show_count').html(data.cart_count);
                $('.num_show').val(data.count);
                $('#total_price').html(data.total_price);
                $('')
            }
        },
        error: function (data) {
            alert(222)
        }
    })
}