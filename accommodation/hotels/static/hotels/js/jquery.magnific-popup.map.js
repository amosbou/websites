$.fn.magnificPopupMap = function(options)
    {
		var default_options = {
			callbacks: null
            };
        options = $.extend({},default_options,options);
		$(this).magnificPopup({
			  type: 'iframe',
			  callbacks: options.callbacks,
			  iframe: {
			    patterns: {
			      googlemap: {
			       
			        index: 'google.com/maps/',
			        
			        id: function(url) {        
			            var m = url.match(/^.+google.com\/maps\/place\/([^_]+)\/?/);
			            if (m !== null) {
			            	var id = m[1].split("/");
			            	return id[0];
			            }
			            return null;
			        },
			        
			        src: 'http://maps.google.com/maps?q=%id%&output=embed'
			        
			      }
			    }
			  }
		});
	};
