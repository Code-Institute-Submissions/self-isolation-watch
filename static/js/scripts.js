/* initialisation for mobile nav bar */
 $(document).ready(function(){
    $('.sidenav').sidenav();
  });

/* initialisation for carousel on welcome page */
    $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });

/* initialisation for date picker on profile form */
  $(document).ready(function(){
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n:{
            done: "select"
        }
    });
  });