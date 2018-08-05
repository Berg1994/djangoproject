//模态框居中的控制
function centerModals() {
    $('.modal').each(function (i) {   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top - 30);  //修正原先已经有的30个像素
    });
}

function setStartDate() {
    var startDate = $("#start-date-input").val();
    if (startDate) {
        $(".search-btn").attr("start-date", startDate);
        $("#start-date-btn").html(startDate);
        $("#end-date").datepicker("destroy");
        $("#end-date-btn").html("离开日期");
        $("#end-date-input").val("");
        $(".search-btn").attr("end-date", "");
        $("#end-date").datepicker({
            language: "zh-CN",
            keyboardNavigation: false,
            startDate: startDate,
            format: "yyyy-mm-dd"
        });
        $("#end-date").on("changeDate", function () {
            $("#end-date-input").val(
                $(this).datepicker("getFormattedDate")
            );
        });
        $(".end-date").show();
    }
    $("#start-date-modal").modal("hide");
}

function setEndDate() {
    var endDate = $("#end-date-input").val();
    if (endDate) {
        $(".search-btn").attr("end-date", endDate);
        $("#end-date-btn").html(endDate);
    }
    $("#end-date-modal").modal("hide");
}

function goToSearchPage(th) {
    var url = "/house/search/?";
    url += ("aid=" + $(th).attr("area-id"));
    url += "&";
    var areaName = $(th).attr("area-name");
    if (undefined == areaName) areaName = "";
    url += ("aname=" + areaName);
    url += "&";
    url += ("sd=" + $(th).attr("start-date"));
    url += "&";
    url += ("ed=" + $(th).attr("end-date"));
    location.href = url;
}

$(document).ready(function () {
    $(".top-bar>.register-login").show();


    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);               //当窗口大小变化的时候
    $("#start-date").datepicker({
        language: "zh-CN",
        keyboardNavigation: false,
        startDate: "today",
        format: "yyyy-mm-dd"
    });
    $("#start-date").on("changeDate", function () {
        var date = $(this).datepicker("getFormattedDate");
        $("#start-date-input").val(date);
    });


    $.get('/house/my_index/', function (data) {
        if (data.code == '200') {

            $('.user-info').show();
            $('.register-login').hide();
            // 展示用户名
            $('.user-name').html(data.user.id_name);


            var index_html_script = template('swiper_script_id', {ohouse: data.houseinfo});

            $('.swiper-wrapper').html(index_html_script);

            var mySwiper = new Swiper('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationClickable: true
            });
        } else {
            $('.user-info').hide();
            $('.register-login').show();
        }
    });

    $.get('/house/area_facility/', function (data) {
        if (data.code == '200') {
            // template 第一个参数填写script的 id   第二个参数填写 返回的data 用键值对表示
            var areas_html_script = template('areas_script_id', {areas: data.areas});
            // 获取标签 填入内容
            $('.area-list').html(areas_html_script)

            $(".area-list a").click(function (e) {
                $("#area-btn").html($(this).html());
                // 此处this 从上面的 area-list a取值
                $(".search-btn").attr("area-id", $(this).attr("area-id"));
                $(".search-btn").attr("area-name", $(this).html());
                // #获取值后隐藏选择模块
                $("#area-modal").modal("hide");
            });

        }
    })

})

