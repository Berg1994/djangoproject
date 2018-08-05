function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(data){

})

$.get('/user/user/',function (data) {
    if(data.code == '200'){
        $('#user-avatar').attr('src','/static/' + data.user_info.avatar)
    $('#user-name').text(data.user_info.name)
    $('#user-mobile').text(data.user_info.phone)

    }
});