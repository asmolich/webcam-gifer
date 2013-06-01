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

});
