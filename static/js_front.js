


function defMeasureFunc(){
window.alert("BEING REROUTED, GOOD LUCK");
window.location.href='https://www.google.com/'
};

function enteringArchiv(){
window.alert('Hello Archivist! Remain Vigilant Of Your Surroundings At All Times When Accessing The Archives!');

}
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("enteringArchiv").addEventListener("click", enteringArchiv);
});

// Wait until the DOM is fully loaded, then attach the event listener
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("defMeasure").addEventListener("click", defMeasureFunc);
});
