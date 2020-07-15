
(function($) {

    'use strict'; 

    /*-----------------------------------------------------------------------------------*/
    /*  Initialize
    /*-----------------------------------------------------------------------------------*/

    new WOW().init();

    /*-----------------------------------------------------------------------------------*/
    /*  Sticky Header
    /*-----------------------------------------------------------------------------------*/
    $(window).scrollTop();
        $(window).scroll(function() {
            if ($(this).scrollTop() > 100) {
                $('.site-header').addClass("fixedwrap");
            } else {
                $('.site-header').removeClass("fixedwrap");
            }
    });

  


    /*-----------------------------------------------------------------------------------*/
    /*  Animsition
    /*-----------------------------------------------------------------------------------*/

    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 1500,
        outDuration: 800,
        linkElement: 'a:not([target="_blank"]):not([href^=#], [class^="image-link"])',
        loading: true,
        loadingParentElement: 'body', //animsition wrapper element
        loadingClass: 'animsition-loading',
        unSupportCss: ['animation-duration',
            '-webkit-animation-duration',
            '-o-animation-duration'
        ],
        overlay: false,

        overlayClass: 'animsition-overlay-slide',
        overlayParentElement: 'body'
    });





    /*-----------------------------------------------------------------------------------*/
    /*  CAROUSEL
    /*-----------------------------------------------------------------------------------*/

    $('.owl-carousel').owlCarousel({
        margin:10,
        dots:true,
        items:4,
        lazyLoad: true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:4
            }
        }
    })


    /*-----------------------------------------------------------------------------------*/
    /*  FLEXSLIDER
    /*-----------------------------------------------------------------------------------*/

    $(".testimonial-wrap .flexslider").flexslider({
        animation: "slide",
        controlNav: true,
        prevText: "",
        nextText: "",
        directionNav: false,
        smoothHeight: false,
        slideshowSpeed: 5000
    });

    $('.class-flexslider').flexslider({
        animation: "fade",
        controlNav: "thumbnails"
    });

    var windowHeight;
    var windowWidth;

    windowHeight = $(window).height();
    windowWidth = $(window).width();

    $(".flexslider-wrap .slides img").each(function() {
        var h = $(this).height();
        var w = $(this).width();
        var ratA = w / h;
        var ratI = windowWidth / windowHeight;
        if (ratA > ratI) {
            var r = w / h;
            $(this).css('height', windowHeight);
            $(this).css('width', windowHeight * r);
            var m = ((windowHeight * r) - windowWidth) / 2;
            $(this).css('margin-left', -m);
            $(this).attr("rat", 1);
            $(this).attr("mar", m);
        } else {
            var r = h / w;
            $(this).css('width', windowWidth);
            $(this).css('height', windowWidth * r);
            var m = ((windowWidth * r) - windowHeight) / 2;
            $(this).css('margin-top', -m);
            $(this).attr("rat", 0);
            $(this).attr("mar", m);
        }
    });

    var windowHeight;
    var windowWidth;

    windowHeight = $(window).height();
    windowWidth = $(window).width();

    $(".fullscreen").css('height', windowHeight);

    $('.flexslider-wrap .slides li').css('height', window.innerHeight - 0);

    /*-----------------------------------------------------------------------------------*/
    /*  SKILL BAR
    /*-----------------------------------------------------------------------------------*/

    $('.skills-bar').each(function() {
        $(this).find('.bar').animate({
            width: $(this).attr('data-percent')
        }, 4000);
    });


})(jQuery); 