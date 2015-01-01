jQuery(document).ready(function($){
    "use strict";
    if ($('.slide-preview-room').length) {
        $('.slide-preview-room .slide-wrapper').find('.bxslider').bxSlider({
            pagerCustom: '#bx-pager',
            auto: true,
            mode: 'fade',
            speed: 500,
            controls: false,
            responsive: true,   
            nextText: '',
            prevText: ''
        });

        

        $('.slide-preview-room .slide-wrapper .bxslider li img')
            .before(function () {
                var srcImg = $(this).attr('src');
                return '<div class="item-img" style="background-image: url(' + srcImg + ')">';
            });
        
        var pagerH = $('#bx-pager').height(),
            headH = $('.md-header').height(),
            windowH = $(window).height(),
            slideH = windowH - headH;
        $('.slide-wrapper .bx-viewport, .slide-wrapper .bxslider').css('height', slideH);
        $(window).on('resize', function() {
                var pagerH = $('#bx-pager').height(),
                headH = $('.md-header').height(),
                windowH = $(window).height(),
                slideH = windowH - headH;
            $('.slide-wrapper .bx-viewport, .slide-wrapper .bxslider').css('height', slideH);
        });


        $('#bx-pager').owlCarousel({
            items: 10,
            itemsCustom: [[0,4], [400,5], [700,8], [1200,10]],
            slideSpeed: 300,
            navigation: false,
            pagination: false,
            addClassActive: true,
            touchDrag: false,
            mouseDrag: false
        });

        var totalActive = $('#bx-pager').find('.owl-item.active').length;
        $('#bx-pager .active:eq('+ totalActive +')').find('.line').hide();
        $('#bx-pager').delegate('.owl-item ', 'click', function() {
            $('#bx-pager').find('.owl-item').css('border', '0');
            if ($(this).prevAll('.active').length == 0) {
                if ($(this).index() > 0) {
                    $(this).find('.line').fadeIn(400);
                    $('#bx-pager').trigger('owl.prev');
                    $('#bx-pager .active:eq('+ totalActive +')').find('.line').fadeOut(500);
                }
            }
            if ($(this).prevAll('.active').length ==  $('#bx-pager').find('.owl-item.active').length -1) {
                if ($(this).index() < $('#bx-pager').find('.owl-item').length -1) {
                    $(this).next().find('.line').fadeOut(400);
                    $(this).find('.line').fadeIn(400);
                    $('#bx-pager').trigger('owl.next');
                } 
            }
        });
    }
});