/* initialisation for mobile nav bar */
 $(document).ready(function(){
    $('.sidenav').sidenav();
  });

/* initialisation for date picker on new symptom form */
  $(document).ready(function(){
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n:{
            done: "select"
        }
    });
/* initialisation for select tool on new symptom  form */
  $(document).ready(function(){
    $('select').formSelect();
  })

/* initialisation for select tool on collapsible function for list of symptoms on symptom landing page */
 $(document).ready(function(){
    $('.collapsible').collapsible();
     })

    });