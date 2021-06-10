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