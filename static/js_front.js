

//This is causing a popup followed by a reroute to the google homepage
function defMeasureFunc(){
window.alert("BEING REROUTED, GOOD LUCK");
window.location.href='https://www.google.com/'
};

// just a popup
function enteringArchiv(){
window.alert('Hello Archivist! Remain Vigilant Of Your Surroundings At All Times When Accessing The Archives!');

}

// Same as below, adding the event listener for entering Archiv
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("enteringArchiv").addEventListener("click", enteringArchiv);
});

// Wait until the DOM is fully loaded, then attach the event listener
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("defMeasure").addEventListener("click", defMeasureFunc);
});

//I think this function is not being used
function flashed(message){
    window.alert(message);
}
