$(document).ready(function() {
    $('#hero_down_button').click(function() {
        console.log("clicked")
        $('#section-about').animate({
            scrollTop:0
        }, 1000);
    });
});