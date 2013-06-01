$('#mainLinkAbout').click(function () {
    $('#canvasHome').addClass('hidden');
    $('#canvasNewCapture').addClass('hidden');
    $('#canvasAbout').removeClass('hidden');
    $('#mainLinkMain').parent().removeClass('active');
    $('#mainLinkAbout').parent().addClass('active');


});


$('#mainLinkMain').click(function () {
    $('#canvasHome').removeClass('hidden');
    $('#canvasNewCapture').addClass('hidden');
    $('#canvasAbout').addClass('hidden');
    $('#mainLinkAbout').parent().removeClass('active');
    $('#mainLinkMain').parent().addClass('active');

});


$('#btnStartNewCapture').click(function () {
    $('#canvasHome').addClass('hidden');
    $('#canvasNewCapture').removeClass('hidden');


    var video = document.getElementById("live")

    navigator.webkitGetUserMedia({video: true },
        function (stream) {
            video.src = window.webkitURL.createObjectURL(stream)
        },
        function (err) {
            console.log("Unable to get video stream!")
        }
    )

});

// initilize video


var snap = function () {
    var live = document.getElementById("live");
    var snapshot = document.getElementById("snapshot");
    var filmroll = document.getElementById("filmroll");

    // Make the canvas the same size as the live video
    snapshot.width = live.clientWidth;
    snapshot.height = live.clientHeight;

    // Draw a frame of the live video onto the canvas
    var c = snapshot.getContext("2d");
    c.drawImage(live, 0, 0, snapshot.width, snapshot.height);

    // Create an image element with the canvas image data
    var img = document.createElement("img");
    img.src = snapshot.toDataURL("image/png");
    img.style.padding = 5;
    img.width = snapshot.width / 2;
    img.height = snapshot.height / 2;

    // Add the new image to the film roll
    filmroll.appendChild(img);


};


$('#btnTakePicture').click(snap);


