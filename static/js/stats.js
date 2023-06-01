const hackerrank = document.querySelector("#hackerrank");
const codechef = document.querySelector("#codechef");
const leetcode = document.querySelector("#leetcode");
const codeforces = document.querySelector("#codeforces");
const spoj = document.querySelector("#spoj");

// hide all contest categories initially
hide(hackerrank);
hide(codechef);
hide(leetcode);
hide(codeforces);
hide(spoj);

function show(container) {
  container.style.display = "block";
}

function hide(container) {
  container.style.display = "none";
}

function handleClick(container) {
  hide(hackerrank);
  hide(codechef);
  hide(leetcode);
  hide(codeforces);
  hide(spoj);
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
hackerrank.querySelector("h4").addEventListener("click", (event) => showCategory("hackerrank", event));
codechef.querySelector("h4").addEventListener("click", (event) => showCategory("codechef", event));
leetcode.querySelector("h4").addEventListener("click", (event) => showCategory("leetcode", event));
codeforces.querySelector("h4").addEventListener("click", (event) => showCategory("codeforces", event));
spoj.querySelector("h4").addEventListener("click", (event) => showCategory("spoj", event));
