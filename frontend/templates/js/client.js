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

$('#btnNewCapture').click(function () {
    $('#canvasHome').addClass('hidden');
    $('#canvasNewCapture').removeClass('hidden');
});

$('#btnControlCapture').click(function () {
    var b = $('#btnControlCapture');
    if (b.hasClass('btn-danger')) {

        b.removeClass('btn-danger').addClass('btn-primary');
        b.html('Continue capture');
    } else {
        b.addClass('btn-danger').removeClass('btn-primary');
        b.html('Interrupt capture');
    }
});

var movie = [];

$('#btnStartCapture').click(function (imageList) {


    return function () {
        var cc = $('#canvasCapture');
        $('#canvasNewCapture').addClass('hidden');
        cc.removeClass('hidden');

        var pos = $('#live').position();

        var d = $('<div style="position: absolute; background-color: white; width: 800; height: 600; z-index: 100;"></div>');
        cc.append(d);
        console.log(pos);
        d.css(pos);

        // initialize video
        var video = document.getElementById("live");

        navigator.webkitGetUserMedia({video: true },
            function (stream) {
                video.src = window.webkitURL.createObjectURL(stream)

                var f = $('#formCaptureParameters');
                var limit = f.find('select[name=captureDuration]').val() * 1000;
                var interval = f.find('select[name=captureInterval]').val() * 1000;

                var timer = setInterval(function () {
                    console.log('acquiring snapshot');
                    snap();

                }, interval);

                setTimeout(function (t, camera) {

                    return function () {
                        camera.stop();
                        clearInterval(t);


                        $('#canvasCapture').addClass('hidden');
                        $('#filmroll').addClass('hidden');
                        $('#canvasVideoOutput').addClass('hidden');

                        var animated = $('#canvasAnimatedCapture');
                        animated.removeClass('hidden');

                        console.log('list:', imageList);
                        var url = 'http://troll-with-friends.appspot.com/upload'; //upload?' + imageList;

                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', url, true);
                        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

                        xhr.responseType = 'blob';
                        xhr.onload = function (e) {

                            console.log('asdf');
                        };

                        var d = [];
                        for (var i in imageList) {
                            d.push(imageList[i].replace('data:image/octet-stream;base64,', ''));
                        }

                        xhr.send('file=' + JSON.stringify(d));

                    }
                }(timer, stream), limit);

            },
            function (err) {
                console.log("Unable to get video stream!")
            }
        )
    }
}(movie));


var snap = function (m) {
    return function () {
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
        var png = snapshot.toDataURL("image/png");

        m.push(png.replace("image/png", "image/octet-stream"));

        img.src = png;
        img.style.padding = 5;
        img.width = 372;
        img.height = 279;

        // Add the new image to the film roll
        $(filmroll).children().remove();
        filmroll.appendChild(img);

    }
}(movie);

