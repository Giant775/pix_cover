/**
 * Scroll UP DOWN Menu
 */
(function ($){
	const body = document.body;
	const headerSlector = document.querySelector(".site-header");
	const scrollUp = "scroll-up";
	const scrollDown = "scroll-down";
	const headerScroll = "headerScrollOn";
	let lastScroll = 0;

	window.addEventListener("scroll", () => {
		const currentScroll = window.pageYOffset;
		if (currentScroll <= 0) {
			body.classList.remove(scrollUp);
			headerSlector.classList.remove(headerScroll);
			return;
		}else{
			headerSlector.classList.add(headerScroll);
		}

		if (currentScroll > lastScroll && !body.classList.contains(scrollDown)) {
			body.classList.remove(scrollUp);
			body.classList.add(scrollDown);
		} else if (
			currentScroll < lastScroll &&
			body.classList.contains(scrollDown)
		) {
			body.classList.remove(scrollDown);
			body.classList.add(scrollUp);
		}
		lastScroll = currentScroll;
	});
})(jQuery);

/**
 * Home Category Flickity Slider
 */
$(document).ready(function(){

	var $carousel = $('.carousel').flickity();
	$('.customPreviousBtn').on( 'click', function() {
	  	$carousel.flickity('previous');
	});
	$('.customNextBtn').on( 'click', function() {
	  	$carousel.flickity('next');
	});

});

/**
 * ISO-TopeProfile Filter
 */
jQuery(document).ready(function() {

	$('.pixSelect2').select2();

    var pixIsotopeGrid = jQuery('#pixProfileFilter, .pixModalProfileLists .pix-profile-filter').isotope();

    jQuery('#profileFilterCat').on( 'change', function() {
        var filterValue = $(this).val();
        pixIsotopeGrid.isotope({ filter: filterValue });
    });
});

/**
 * Messenger Container
 */
jQuery(document).ready(function() {

	$('.pix-msng-mobile .msng-chat-navbar .msng-chat-nav-item').on('click', function (){
		$('.pix-msng-mobile .msgn-mobile-chat-container').addClass('chatOpen');
	});

	$('.pix-msng-mobile .msgn-profile-back').on('click', function (){
		$('.pix-msng-mobile .msgn-mobile-chat-container').removeClass('chatOpen');
	});

});


/**
 * Toggle menu
 */
(function($) {
	"use strict";

	var toggleMenu 	  = $('.toggleMenu'),
		stickyMenuBox = $('.stickyMenuBox'),
		menuOutSider  = $('.menuOutSider'),
		menuItemClass = $('.menuContent .manuContentWrap .navbar-nav li:not(.menu-item-has-children) > a');

	function menuOpen() {
		toggleMenu.toggleClass('open');
		stickyMenuBox.toggleClass('menuOpen');
		menuOutSider.toggleClass('openMask');
		$('body').toggleClass('scrollOff');
		// menuItemClass.toggleClass('animated fadeInRight');
	}

	function menuClose() {
		toggleMenu.removeClass('open');
		stickyMenuBox.removeClass('menuOpen');
		menuOutSider.removeClass('openMask');
		$('body').removeClass('scrollOff');
		// menuItemClass.removeClass('animated fadeInRight');
	}

	toggleMenu.on('click', function () {
		menuOpen();
	});

	$(document).click(function(e) {
	    if ( $(e.target).is( menuOutSider ) || $(e.target).is( menuItemClass ) ) {
	    	menuClose();
	    }
	});

	$(document).ready(function(){
		$(".menuContent ul.navbar-nav > li.menu-item-has-children > a").click( function(e) {
			e.preventDefault();
	    	var target = $(this).parent().children(".sub-menu");
	    	$(target).slideToggle('slow');
	    	$(this).toggleClass('menuExpandOpen');
	  	});

	  	// $(".profile-navbar .profileToggleMenu").click( function(e) {
		// 	e.preventDefault();
	    // 	$(".profile-navbar").toggleClass('pixMenuOpen');
	  	// });
	});

})(jQuery);

/**
 * Work Setting Tab
 */
(function($) {
	$(document).ready(function(){
        $('.pix-tab-menu a.pix-setting-menu-item').click(function(e){
        	e.preventDefault();
            $('.pix-tab-menu a.pix-setting-menu-item').removeClass('active');
            $(this).addClass('active');

            var tagid = $(this).data('pixtab');
            $('.pix-tab-content').removeClass('pix-show').addClass('hide');
            $('#'+tagid).addClass('pix-show').removeClass('hide');
        });

        $('.pix-select-box .select-list-title').click(function(e){
        	e.preventDefault();
        	$(this).next('.pix-select-dropdown').slideToggle();
        });
    });

})(jQuery);


/**
 * Profile Details Modal
 */
(function() {

	$(document).ready(function(){

		const pixCarousel = $('.owl-carousel');
		pixCarousel.owlCarousel({
			nav: true,
			dots: false,
			loop: false,
			margin: 0,
			items: 1,
			startPosition: 0,
			autoHeight: true,
			touchDrag: false,
			mouseDrag: false,
			video: true,
			responsive: {
			    0: {
			    	touchDrag: true,
					mouseDrag: true,
					nav: true,
					autoHeight: true,
			    },
			    991: {
			    	touchDrag: false,
					mouseDrag: false,
					nav: true,
					autoHeight: false,
			    }
		  	}
		});


		$(".profileDetailsSlider").on('translate.owl.carousel', function (e) {
			$('.owl-item .item video').each(function () {
				$(this).get(0).play();
			});
		});

		$(".profileDetailsSlider").on('translated.owl.carousel', function (e) {
			if ($('.owl-item.active').find('video').length !== 0) {
				var videoItem = $('.owl-item.active .item video');
				$(this).currentTime = 0;
				videoItem.get(0).play();
			}
		});

		$(".pixDetailsModal, .pixModalClose").on("click", function (e) {
			if ($('.pixDetailsModal.pixModal-active').find('video').length !== 0) {
				var videoItem = $('.pixDetailsModal.pixModal-active .owl-item.active video');
				$(this).currentTime = 0;
				videoItem.get(0).play();
			}
		});

	    function closestEl(el, selector) {
	        var doc = el.document || el.ownerDocument;
	        var matches = doc.querySelectorAll(selector);
	        var i;
	        while (el) {
	            i = matches.length - 1;
	            while (i >= 0) {
	                if (matches.item(i) === el) {
	                    return el;
	                }
	                i -= 1;
	            }
	            el = el.parentElement;
	        }
	        return el;
	    }

	    var videoSlector = document.querySelector(".pixModal-active .modalVideo");
	    var pixModalIsotopeGrid = jQuery('.pixModalProfileLists .pix-profile-filter').isotope();
	    var zIndex = 99999;
	    var pixDetailsModalContainer = $(".pixDetailsModal");
		var owl = $(".profileDetailsSlider");
		var modalScrollTop = $('.pixDetailsModal');

	    var modalBtns = document.querySelectorAll(".pixDataModalItem");
		    modalBtns.forEach(function addBtnClickEvent(btn) {
		        btn.onclick = function showModal() {
		            var modal = btn.getAttribute("data-modal");
		            if(typeof modal !== null && modal !== 'undefined' ) {
		            	pixDetailsModalContainer.animate({ scrollTop: 0 }, 'slow');
		            	pixDetailsModalContainer.removeClass("pixModal-active");
		            	document.getElementById(modal).classList.add("pixModal-active");
		            	document.getElementById(modal).style.zIndex = zIndex++;
		            	document.body.classList.add('scrollOff');
		            	pixModalIsotopeGrid.isotope();
					}
		        };
		    });

		function closeModalDetails() {
			document.body.classList.remove('scrollOff', 'scroll-down');
			pixDetailsModalContainer.removeClass("pixModal-active");
			pixDetailsModalContainer.animate({ scrollTop: 0 }, 'slow');
            pixModalIsotopeGrid.isotope('destroy');
            pixModalIsotopeGrid.isotope();
    		owl.trigger('to.owl.carousel', 0);

    		if( videoSlector ){
    			videoSlector.load();
            	videoSlector.currentTime = 0;
    		}
		}

	    var closeBtns = document.querySelectorAll(".pixModalClose");
		    closeBtns.forEach(function addCloseClickEvent(btn) {
		        btn.onclick = function closeModal() {
		            var modal = closestEl(btn, ".pixDetailsModal");
		            if(typeof modal !== null && modal !== 'undefined' ) {
		            	closeModalDetails();
			        }
		        };
		    });

		document.addEventListener("click", function(e) {
			var modalOuter = document.querySelector('.pixModal-active');
			if (modalOuter && e.target == modalOuter) {
				closeModalDetails();
			}
		});
	});
}());



/**
 * Preloading Item
 */
(function($) {
	$(window).on("load", function() {
        setTimeout( () => {

            $('.pixLoading').removeClass('pixLoading').addClass('pix__fadeIn');

        }, 3000);
    });

})(jQuery);


/**
 * Lazyload Images
 */
(function($) {

	const lazy = () => {
		document.addEventListener('lazyloaded', (e) => {
			e.target.parentNode.classList.add('image-loaded');
			e.target.parentNode.classList.remove('loading');
		});
	}
	lazy();

})(jQuery);

/**
 * Scroll Menu
 */
(function() {
	var container = document.getElementById('scrollContainer');
    var isDown = false;
    var startX;
    var scrollLeft;

    if(container){
	    container.addEventListener('mousedown', function(e) {
	        isDown = true;
	        startX = e.pageX - container.offsetLeft;
	        scrollLeft = container.scrollLeft;
	    });

	    container.addEventListener('mouseleave', function() {
	        isDown = false;
	    });

	    container.addEventListener('mouseup', function() {
	        isDown = false;
	    });

	    container.addEventListener('mousemove', function(e) {
	        if (!isDown) return;
	        e.preventDefault();
	        var x = e.pageX - container.offsetLeft;
	        var walk = (x - startX) * 3;
	        container.scrollLeft = scrollLeft - walk;
	    });
    }

})();


/**
 * Search Filter Modal
 */
(function($) {
	$(document).ready(function(){
        $('.pix-mobile-src-filter-btn').click(function(){
            $('body').toggleClass('scrollOff');
            $('.pix-filter-modal').toggleClass('filterOpen');
        });
        $('#modalFilterSubmit, .pix-filter-mask').click(function(){
            $('body').removeClass('scrollOff');
            $('.pix-filter-modal').removeClass('filterOpen');
        });
    });

})(jQuery);



