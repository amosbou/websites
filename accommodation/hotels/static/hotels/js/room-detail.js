jQuery(document).ready(function($){
	"use strict";
	$('.bxslider').bxSlider({
		pagerCustom: '#bx-pager',
		auto: true,
		mode: 'fade',
		speed: 500,
		controls: true,
		responsive: true,	
		nextText: '',
		prevText: '',
		adaptiveHeight: true,
		onSliderLoad: function(){
			$('.bx-prev').html('<i class="icon icon-previous"></i>'); 
			$('.bx-next').html('<i class="icon icon-next"></i>');
			// $(window).resize(function(){
			// 	var w0 =$(".md-slide img").width(),
			// 		w1 = $(window).width()/2,
			// 		w2 = w0/2,
			// 		w = w2 - w1;
			// 		$(".bx-viewport").width(w0).css("left",-w);
			// 		console.log(w);
			// }).trigger('resize');
		}
	});
});