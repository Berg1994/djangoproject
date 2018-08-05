function logout() {
    $.get("/my_user/logout/", function (data) {
        if (data.code == '200') {
            location.href = "/my_user/login/";
        }
    })
}

$(document).ready(function () {

    $.get('/my_user/userinfo/', function (data) {
        if (data.code == '200') {

            $('#user-name').text(data.user_info.name);
            $('#user-mobile').text(data.user_info.phone);
            $('#user-avatar').attr('src', '/static/media/' + data.user_info.avatar)
        }
    })


})