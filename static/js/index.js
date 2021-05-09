$(document).ready(function () {
    
    $(this).scrollTop(0);
    $('body').append('<div id="toTop" class="btn btn-info"><span class="glyphicon glyphicon-chevron-up"></span> Back to Top</div>');

    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $('#toTop').fadeIn();
        }
        else {
            $('#toTop').fadeOut();
        }
    });


    $('#toTop').click(function () {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });


    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll > 100) {
            $("nav").addClass("navbarscroll");
        }
        else {
            $("nav").removeClass("navbarscroll");
        }
    });

    $("body").bind("keydown", function(e){
        if(e.keyCode == 44 ){
            return false;
        }
    });

});
