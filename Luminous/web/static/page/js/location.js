function myMap() {
  var mapCanvas = document.getElementById("map");
  var myCenter = new google.maps.LatLng(37.51107250301698, 127.05733066064631);
  var infowindow = new google.maps.InfoWindow({
  content: "LUMINOUS"});
  infowindow.open(map,marker);
  var mapOptions = {
    center: myCenter,
    zoom: 15
  };
  var map = new google.maps.Map(mapCanvas, mapOptions);
  var star = new google.maps.MarkerImage("img/star.png", null, null, null, new google.maps.Size(55,55));
  var marker = new google.maps.Marker({
  position:myCenter,
  animation:google.maps.Animation.BOUNCE,
  icon: star,
  });
  marker.setMap(map);
  
  var infowindow = new google.maps.InfoWindow({
      content: "LUMINOUS"
    });
    infowindow.open(map,marker);
  
  var myUniversity = new google.maps.Circle({
    center: myCenter,
    radius: 100,
    strokeColor: "skyblue",
    strokeOpacity: 0.5,
    strokeWeight: 3,
    fillColor: "skyblue",
    fillOpacity: 0.3
  });
  myUniversity.setMap(map);
  }
  
  function func(){
  var name= document.getElementById("name").value;
  var email= document.getElementById("email").value;
  var comments = document.getElementById("comments").value;
  
  if(name==""||email==""||comments==""){
    alert("Please fill in all the blanks.");
    return false;
  }
  if(confirm("Name : "+name+"\nEmail : "+email+ "\nComments : "+comments+ "\n\nIs the name and the contents written correct?")==true){
  alert("submit complete!");
  location.reload();
  }
    else{
      return;
    }
  
  }
  