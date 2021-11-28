function joinalert() {
  var id = document.getElementById("username").value;
  var pw = document.getElementById("password1").value;
  var pwcon = document.getElementById("password2").value;
  var name = document.getElementById("name").value;
  var phone = document.getElementById("phone").value;
  var addr = document.getElementById("address").value;
  if (id.length != 0 && pw.length != 0 && pwcon.length != 0 && name.length != 0 && phone.length != 00 && addr.length != 00) {
    alert("Congratulations on your membership!");
  }
  else {
    alert("Please fill in all the blanks.");
  }
}

function con() {
  var pw = document.getElementById("password1").value;
  var pwcon = document.getElementById("password2").value;

  if (pw.length < 8 || pwcon.length < 8) {
    alert("Password is 8 characters or less. Please use another password.");
  }
  else if(pw != pwcon){
    alert("Password and password comfirmation is not same.")
  }
  else{
    alert("This is an acceptable password.");
  }
}
