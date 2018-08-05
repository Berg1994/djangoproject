function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}


$(document).ready(function () {
    auth();
    $('#form-auth').submit(function (e) {
        e.preventDefault();
        real_name= $('#real-name').val();
        id_card = $('#id-card').val();
       $.ajax({
           url:'/my_user/auth/',
           data:{'real_name':real_name,'id_card':id_card},
           dataType:'json',
           type:'PATCH',
           success:function (data) {
              auth()
           },
           error:function (data) {
               alert('请求失败')
           }
       })

    });


});

function auth() {
        $.get('/my_user/real_user_info/',function (data) {
        if(data.code == '200'){
            $('#real-name').val(data.user.id_name);
            $('#id-card').val(data.user.id_card);
            if(data.user.id_name){
                $('.btn-success').hide()
            }


        }
    })
}
