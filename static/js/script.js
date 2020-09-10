document.addEventListener("DOMContentLoaded", () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach((el) => {
      el.addEventListener("click", () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle("is-active");
        $target.classList.toggle("is-active");
      });
    });
  }
});

const modal = document.querySelector(".modal");
const modalbackground = document.querySelector(".modal-background");
const modalclose = document.querySelector(".modal-close");

console.log(document.querySelectorAll("#login"));

document.querySelectorAll("#login")[0].addEventListener("click", () => {
  modal.classList.add("is-active");
});

document.querySelectorAll("#login")[1].addEventListener("click", () => {
  modal.classList.add("is-active");
});

modalbackground.addEventListener("click", () => {
  modal.classList.remove("is-active");
});
modalclose.addEventListener("click", () => {
  modal.classList.remove("is-active");
});
