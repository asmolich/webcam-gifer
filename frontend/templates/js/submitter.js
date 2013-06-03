alert('wohoo');
console.log('context');

window.addEventListener("message", function (event) {
    console.info("message received in sandbox: " + event.data.message);
});