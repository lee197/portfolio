$(function(){"use strict";var wind=$(window);$(".navbar-nav").singlePageNav({speed:1e3,currentClass:"active",offset:60});wind.on("scroll",function(){var bodyScroll=wind.scrollTop(),navbar=$(".navbar");if(bodyScroll>300){navbar.show()}else{navbar.hide()}});$(".caption h4 span").typed({strings:["iOS Developer","Python Django Developer","Android Developer", "Drone Photographer"],loop:true,startDelay:1e3,backDelay:2e3});$(".button-scroll").on("click",function(){var scrollTo=$(this).attr("data-scrollTo");$("body, html").animate({scrollTop:$("#"+scrollTo).offset().top-60},1e3)});wind.on("scroll",function(){$(".progress-main .progress-bar").each(function(){var bottom_of_object=$(this).offset().top+$(this).outerHeight();var bottom_of_window=$(window).scrollTop()+$(window).height();var myVal=$(this).attr("data-value");if(bottom_of_window>bottom_of_object){$(this).css({width:myVal})}})});$(".v-middle").magnificPopup({delegate:"a",type:"image"});$(".counter").counterUp({delay:10,time:1500});$(".blog .owl-carousel").owlCarousel({loop:true,mouseDrag:false,autoplay:true,smartSpeed:500,dots:false,margin:30,responsiveClass:true,responsive:{0:{items:1},600:{items:2},1e3:{items:3}}});$(".clients .owl-carousel").owlCarousel({items:1,loop:true,mouseDrag:false,autoplay:true,smartSpeed:500});wind.stellar();$(".gallery").isotope({itemSelector:".item-img"});var $gallery=$(".gallery").isotope({});$(".filtering").on("click","span",function(){var filterValue=$(this).attr("data-filter");$gallery.isotope({filter:filterValue})});$(".filtering").on("click","span",function(){$(this).addClass("active").siblings().removeClass("active")})});$(window).on("load",function(){$(".loading").fadeOut(500);$("#contact-form").validator();$("#contact-form").on("submit",function(e){if(!e.isDefaultPrevented()){var url="contact.php";$.ajax({type:"POST",url:url,data:$(this).serialize(),success:function(data){var messageAlert="alert-"+data.type;var messageText=data.message;var alertBox='<div class="alert '+messageAlert+' alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>'+messageText+"</div>";if(messageAlert&&messageText){$("#contact-form").find(".messages").html(alertBox);$("#contact-form")[0].reset()}}});return false}})});
