console.log("hi umaaaa")

event.preventDefault();
const button = document.getElementByClass("btn btn-outline-primary rounded")
const thankYou = document.getElementById("thank-you-message")
//whenever the button is clicked, toggle the ".hidden" class
button.addEventListener("click", ()=>{
      thankYou.classList.toggle("hidden")
})