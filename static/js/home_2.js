/*global $, console, alert, jQuery*/

/*$(function () {
    
    'use strict';
    // Slider Hieght
    var upperH = $('.top-bar').innerHeight(),
        navH = $('.navbar').innerHeight(),
        hSum = (upperH + navH) * -1;
    $('.header').css('margin-top', hSum);
});*/

$(document).ready(function () {
    
    'use strict';
    
    $('.box').on('click', 'li', function () {
        
        var tabId =  $(this).attr('id');
        
        $(this).addClass('active').siblings().removeClass('active');
        
        $('#' + tabId + '-cont').addClass('active').siblings().removeClass('active');
    
    });
});

//slider owl
$('.slider-carousal').owlCarousel({
    loop: true,
    margin: 10,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: true,
            dots: false
        },
        600: {
            items: 2,
            nav: true,
            dots: false
        },
        1000: {
            items: 4,
            nav: true,
            loop: false,
            dots: false
        }
    }
});

//slider owl
$('.slider-count').owlCarousel({
    loop: true,
    margin: 10,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: true,
            dots: false
        },
        600: {
            items: 3,
            nav: true,
            dots: false
        },
        1000: {
            items: 6,
            nav: true,
            loop: false,
            dots: false
        }
    }
});
$('#datepicker1').datepicker({
            uiLibrary: 'bootstrap4'
        });  
	 $('#datepicker2').datepicker({
            uiLibrary: 'bootstrap4'
        }); 