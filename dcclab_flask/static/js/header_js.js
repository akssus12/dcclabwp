$(document).ready( function() {

    $("#header .hamb").click(function(){
       $("#header #h_menu").addClass("show");
    });
    
    $("#header .cross").click(function(){
       $("#header #h_menu").removeClass("show");
    });
});


