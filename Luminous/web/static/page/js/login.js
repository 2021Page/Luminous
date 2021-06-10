function loginalert() {
  var id = document.getElementById("username").value;
  var pw = document.getElementById("password").value;
  if (id.length == 0 && pw.length == 0) {
    alert("ID, Password are required!!");
  }
  else if (id.length == 0 && pw.length != 0) {
    alert("ID is required!!");
  }
  else if (id.length != 0 && pw.length == 0) {
    alert("Password is required!!");
  }
  else {
    alert("Welcome to Luminous <" + id + ">");
  }
}
