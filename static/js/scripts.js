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
    }
    )});
/* initialisation for select tool on new symptom  form */
  $(document).ready(function(){
    $('select').formSelect();
  })

/* initialisation for select tool on collapsible function for list of symptoms on symptom landing page */
 $(document).ready(function(){
    $('.collapsible').collapsible();
     })
/* initialisation for dropdown tool on for list of symptoms on my_symptoms page */     
  $('.dropdown-trigger').dropdown();

/* initialisation for carousel on welcome page */  
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });

/* initialisation for modals for double checking deleting */  
  $(document).ready(function(){
    $('.modal').modal();
  });

/* copying the site URL */ 

let clipboard = new ClipboardJS('.copy-btn');
// If copy to clipboard function is successful
clipboard.on('success', function(e) {
    $('.copy-btn').append('<p class="small-titles">Copied!</p>');
});
// If copy to clipboard function is not supported by users' browser, an error is triggered here
clipboard.on('error', function(e) {
alert("Oops, it looks like this function isn't supported on your browser! Don't worry, Just copy this: https://self-isolation-watch.herokuapp.com/");

});
// scroll to top
const scroller = document.querySelector(".scroller");
window.addEventListener("scroll" , () => {
    if (window.pageYOffset>100){
        scroller.classList.add("active");
    } else {scroller.classList.remove("active");
}
});