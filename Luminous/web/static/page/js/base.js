function func() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var comments = document.getElementById("comments").value;

  if (name == "" || email == "" || comments == "") {
    alert("Please fill in all the blanks.");
    return false;
  }
  if (confirm("Name : " + name + "\nEmail : " + email + "\nComments : " + comments + "\n\nIs the name and the contents written correct?") == true) {
    alert("submit complete!");
    location.reload();
  }
  else {
    return;
  }

}

function goTop() {
  window.scrollTo(0, 0);
}

function goBottom() {
  document.getElementById('bottom').scrollIntoView();
}
window.addEventListener("resize", function () {
    "use strict"; window.location.reload();
});

document.addEventListener("DOMContentLoaded", function () {
    if (window.innerWidth > 992) {
        document.querySelectorAll('.nav-item').forEach(function (everyitem) {
            everyitem.addEventListener('mouseover', function (e) {
                let el_link = this.querySelector('a[data-bs-toggle]');
                if (el_link != null) {
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.add('show');
                    nextEl.classList.add('show');
                }
            });
            everyitem.addEventListener('mouseleave', function (e) {
                let el_link = this.querySelector('a[data-bs-toggle]');
                if (el_link != null) {
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.remove('show');
                    nextEl.classList.remove('show');
                }
            })
        });
    }
});
