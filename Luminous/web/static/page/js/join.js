function joinalert(){
  var id = document.getElementById("a").value;
  var pw = document.getElementById("b").value;
  var pwcon = document.getElementById("c").value;
  var name = document.getElementById("d").value;
  var phone = document.getElementById("e").value;
  var addr = document.getElementById("f").value;
  if(id.length!=0&&pw.length!=0&&pwcon.length!=0&&name.length!=0&&phone.length!=00&&addr.length!=00){
    alert("Congratulations on your membership!");
    window.location.href = "login.html";
  }
  else{
    alert("Please fill in all the blanks.");
}
}
