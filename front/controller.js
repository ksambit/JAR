$(document).ready(function() {
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        // stop any running animations, show message and keep it visible a bit longer
        $(".siri-message").stop(true, true).fadeIn(100).delay(3000).fadeOut(200);
    }

    eel.expose(ShowHood)
    function ShowHood(){
        // return to home screen after a short delay
        (function(){
            function goHome(){
                if ($('#home').length) {
                    $('.screen').hide();
                    $('#home').fadeIn(200);
                } else if ($('.home-screen').length) {
                    $('.screen').hide();
                    $('.home-screen').fadeIn(200);
                } else if ($('.home-button').length) {
                    $('.home-button').trigger('click');
                } else {
                    // fallback: navigate to root or reload
                    if (location.pathname !== '/' && location.pathname.toLowerCase().indexOf('index') === -1) {
                        location.href = '/';
                    } else {
                        location.reload();
                    }
                }
            }

            // small delay so any command UI can finish before returning
            setTimeout(goHome, 500);
        })();

    }
    
});
 