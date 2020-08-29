const modalonetimelogin = document.querySelector(".modal.onetimelogin");
const modal = document.querySelectorAll(".modal")[1];
const modalbackgroundonetimelogin = document.querySelector(".modal-background");
const modalbackground = document.querySelectorAll(".modal-background")[1];

document.querySelector("#onetimelogin").addEventListener("click", () => {
  modalonetimelogin.classList.add("is-active");
});

document.querySelector("#login").addEventListener("click", () => {
  modal.classList.add("is-active");
});

modalbackground.addEventListener("click", () => {
  modal.classList.remove("is-active");
});

modalbackgroundonetimelogin.addEventListener("click", () => {
  modalonetimelogin.classList.remove("is-active");
});

document
  .querySelector(".modal-close.is-large")
  .addEventListener("click", () => {
    modal.classList.remove("is-active");
  });

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
