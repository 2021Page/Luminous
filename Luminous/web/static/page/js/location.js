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
  var star = new google.maps.MarkerImage("/static/page/img/star.png", null, null, null, new google.maps.Size(55,55));
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
  