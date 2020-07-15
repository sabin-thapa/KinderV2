
$(document).ready(function() {

var scrollLink = $('.scroll');

// Smooth scrolling
scrollLink.click(function(e) {
e.preventDefault();
$('body,html').animate({
scrollTop: $(this.hash).offset().top
},1000 );
});


})



 jQuery(document).ready(function() {
       var offset = 500;
       var duration = 300;
       var a=1000;
       jQuery(window).scroll(function() {
       if (jQuery(this).scrollTop() > offset) {
       jQuery('.back-to-top').fadeIn(duration);
       } else {
       jQuery('.back-to-top').fadeOut(duration);
       }
       });
       jQuery('.back-to-top').click(function(event) {
      file:
       event.preventDefault();
       jQuery('html, body').animate({scrollTop: 0}, a);
       return false;
       })
 })
