


function defMeasureFunc(){
window.alert("BEING REROUTED, GOOD LUCK");
window.location.href='https://www.google.com/'
};

// Wait until the DOM is fully loaded, then attach the event listener
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("defMeasure").addEventListener("click", defMeasureFunc);
});
