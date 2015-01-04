
(function ($) { 
/* NATION theme script initializing */
$(document).ready(function() {

	// Function for read cookie
	function readCookie(name) {
		var nameEQ = name + "=";
		var ca = document.cookie.split(';');
		for(var i=0;i < ca.length;i++) {
			var c = ca[i];
			while (c.charAt(0)==' ') c = c.substring(1,c.length);
			if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
		}	
		return null;
	}
	
	// Style switcher initialize 
	$('#style-switcher').on("click",function(){ 
		
		if ($('#style-form').css("display")=='none') {
			$('#style-form').show();
			$('#style-switcher').css({'left':'135px','padding-left':'13px'}); 
		} else {
			$('#style-form').hide();
			if ( readCookie('layout') != 'boxed' ) {
				$('#style-switcher').css({'left':'0px','padding-left':'13px'}); 
			} else {
				$('#style-switcher').css({'left':'0px','padding-left':'13px'}); 
			}
		}
	});
	
	$("#layout-select").change(function(){
		if ( $(this).val() == 'boxed' ) {
			$("#style-switcher").css({'padding-left':'12px'});
			document.cookie="layout=boxed";
			location.reload();
		} else if ( $(this).val() == 'wide' ) {
			$("#style-switcher").css({'padding-left':'12px'});
			document.cookie="layout=wide";
			location.reload();
		}
	});
	
	var switcher_layout = readCookie('layout');
		
	$("#bg-image1").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_boxed_image.css');
			$("body").css('background-image','url(images/background-image1.jpg)');
			document.cookie="background=bg1";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	$("#bg-image2").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_boxed_image.css');
			$("body").css('background-image','url(images/background-image2.jpg)');
			document.cookie="background=bg2";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	$("#bg-pattern1").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_pattern.css');
			$("body").css('background-image','url(images/tileable_wood_texture.png)');
			document.cookie="background=bgp1";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	$("#bg-pattern4").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_boxed_wood.css');
			document.cookie="background=bgp4";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	$("#bg-pattern3").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_boxed_grunge.css');
			document.cookie="background=bgp3";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	$("#bg-pattern2").click(function(){
		if ( switcher_layout == 'boxed') {
			$("link[href^='css/style']").attr('href','css/style_boxed_wall.css');
			document.cookie="background=bgp2";
			location.reload();
		} else {
			alert('You should switch to boxed layout first.');
		}
	});
	
	var background_cookie = readCookie('background');
	
	$("#color-scheme1").click(function(){
		document.cookie="pcolor=c49456";
		document.cookie="scolor=677c8b";
		location.reload();
	});
	$("#color-scheme2").click(function(){
		document.cookie="pcolor=d46857";
		document.cookie="scolor=677c8b";
		location.reload();
	});
	$("#color-scheme3").click(function(){
		document.cookie="pcolor=c49456";
		document.cookie="scolor=424242";
		location.reload();
	});
	$("#color-scheme4").click(function(){
		document.cookie="pcolor=d46857";
		document.cookie="scolor=424242";
		location.reload();
	});
	
	var color_cookie = readCookie('color');
		
		
	if ( switcher_layout == 'boxed' ) {
		$("#layout-select option[value='boxed']").attr('selected','selected');
		$("#style-switcher").css({'padding-left':'10px'});
		if ( $(window).width() > 1060 && $(window).width() < 1290 ) { $("#wrapper").css("width","1060px"); }
		if ( $(window).width() > 1290 ) { $("#wrapper").css("width","1320px"); }
	} else if ( switcher_layout == 'wide' ) {
		$("#layout-select option[value='wide']").attr('selected','selected');
		$("#style-switcher").css({'padding-left':'10px'});
	} 
	
	if ( background_cookie == 'bg1' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_boxed_image.css');
		$("body").css('background-image','url(images/background-image1.jpg)');
		$("#back-to-top").css('border-color','#fff').children('span').css('color','#fff');
	} else if ( background_cookie == 'bg2' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_boxed_image.css');
		$("body").css('background-image','url(images/background-image2.jpg)');
		$("#back-to-top").css('border-color','#fff').children('span').css('color','#fff');
	} else if ( background_cookie == 'bgp1' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_pattern.css');
		$("body").css('background-image','url(images/tileable_wood_texture.png)');
	} else if ( background_cookie == 'bgp4' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_pattern.css');
		$("body").css('background-image','url(images/bgnoise_lg.png)');
	} else if ( background_cookie == 'bgp3' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_pattern.css');
		$("body").css('background-image','url(images/squairy_light.png)');
	} else if ( background_cookie == 'bgp2' && switcher_layout == 'boxed' ) {
		$("link[href^='css/style']").attr('href','css/style_pattern.css');
		$("body").css('background-image','url(images/subtle_white_feathers.png)');
	}
	
	if ( color_cookie == "red" ) {
		$("#main-header-wrap").css('background-image','url(images/header-bg.png)');
		$(".sub-menu").css('background-image','url(images/submenu-bg.png)');
		$("#header-text").css('border-bottom','1px dotted #e85c76');
		$("#footer-wrap, #copyright-wrap").css('background-image','url(images/caption-bg.png)');
		$(".slider-caption11, .slider-caption12, .slider-caption21, .slider-caption22, .slider-caption31, .slider-caption32").css('background-color','#39cf76');
	} else if ( color_cookie == "pink" ) {
		$("#main-header-wrap, .sub-menu").css('background-image','url(images/header-bg2.png)');
		$("#header-text").css('border-bottom','1px dotted #f974ac');
		$("#footer-wrap, #copyright-wrap").css('background-image','url(images/caption-bg2.png)');
		$(".slider-caption11, .slider-caption12, .slider-caption21, .slider-caption22, .slider-caption31, .slider-caption32").css('background-color','#69C6B9');
	} else if ( color_cookie == "purple" ) {
		$("#main-header-wrap, .sub-menu").css('background-image','url(images/header-bg3.png)');
		$("#header-text").css('border-bottom','1px dotted #9e9be6');
		$("#footer-wrap, #copyright-wrap").css('background-image','url(images/caption-bg3.png)');
		$(".slider-caption11, .slider-caption12, .slider-caption21, .slider-caption22, .slider-caption31, .slider-caption32").css('background-color','#39cf76');
	}

});

})(jQuery);