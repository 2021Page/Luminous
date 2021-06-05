function loginalert(){
  var id = document.getElementById("x").value;
  var pw = document.getElementById("y").value;
  if(id.length==0&&pw.length==0){
    alert("ID, Password are required!!");
  }
  else if(id.length==0&&pw.length!=0){
    alert("ID is required!!");
  }
  else if(id.length!=0&&pw.length==0){
    alert("Password is required!!");
  }
  else{
    alert("Welcome to Luminous <"+id+">");
    document.location.href="main.html";
}
}
