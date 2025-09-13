document.addEventListener("DOMContentLoaded", () => {
    const siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 600,
        height: 200,
        style: "ios9",
        amplitude: 1,
        autostart: true,
    });
});
    // mic button
    $("#mic").click(function () { 
       // Start listening to the user's voice
       $("#Oval").attr("hidden",true);
       $("#Siri-wave").attr("hidden",false);

       eel.takecommand()()
       .then((response) => {
           
           console.log("Response from Python:", response);
       });
    });
    