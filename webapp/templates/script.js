$( ".inner-switch" ).on("click", function() {
    if( $( "body" ).hasClass( "dark-theme" )) {
      $( "body" ).removeClass( "dark-theme" );
      $( ".inner-switch" ).text( "OFF" );
    } else {
      $( "body" ).addClass( "dark-theme" );
      $( ".inner-switch" ).text( "ON" );
    }
});
