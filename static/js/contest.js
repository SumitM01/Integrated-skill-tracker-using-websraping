const ongoing = document.querySelector("#ongoing-contest");
const upcoming = document.querySelector("#upcoming-contest");
const long = document.querySelector("#long-contest");
const expired = document.querySelector("#expired-contest");

// hide all contest categories initially
hide(ongoing);
hide(upcoming);
hide(long);
hide(expired);

function show(container) {
  container.style.display = "block";
}

function hide(container) {
  container.style.display = "none";
}

function handleClick(container) {
  hide(ongoing);
  hide(upcoming);
  hide(long);
  hide(expired);
  show(container);
}

function showCategory(categoryName, event) {
    var i;
    var x = document.getElementsByClassName("category");
    for (i = 0; i < x.length; i++) {
      hide(x[i]); // hide all categories
      var btn = document.querySelectorAll('.category-button')[i];
      btn.classList.remove("active"); // remove "active" class from all buttons
    }
    event.target.classList.add("active"); // add "active" class to the clicked button
    show(document.getElementById(categoryName)); // show the selected category
  }
  

  
  
// add click event listeners to the category headings
ongoing.querySelector("h2").addEventListener("click", () => handleClick(ongoing));
upcoming.querySelector("h2").addEventListener("click", () => handleClick(upcoming));
long.querySelector("h2").addEventListener("click", () => handleClick(long));
expired.querySelector("h2").addEventListener("click", () => handleClick(expired));




  
