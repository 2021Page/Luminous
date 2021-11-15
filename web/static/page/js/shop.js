function OnMouseIn(n) {
  n.style.border = "1.5px solid rgb(128, 146, 199)";
  n.style.backgroundColor = "#EBF5FF";
}
function OnMouseOut(n) {
  n.style.border = "";
  n.style.backgroundColor = "";
}
function image_onclick() {
  var arrImage = new Array("/static/page/img/nail/nail1.png", "/static/page/img/nail/nail2.png", "/static/page/img/nail/nail3.png",
    "/static/page/img/nail/nail4.png", "/static/page/img/nail/nail5.png", "/static/page/img/nail/nail6.png",
    "/static/page/img/nail/nail7.png", "/static/page/img/nail/nail8.png", "/static/page/img/nail/nail9.png",
    "/static/page/img/nail/nail10.png", "/static/page/img/nail/nail11.png", "/static/page/img/nail/nail12.png",
    "/static/page/img/nail/nail13.png", "/static/page/img/nail/nail14.png", "/static/page/img/nail/nail15.png");
  var imgSource = document.targetImg;
  var intRandom = Math.round(Math.random() * 14);
  while (imgSource.src.indexOf(arrImage[intRandom]) != -1) {
    intRandom = Math.round(Math.random() * 14);
  }
  imgSource.src = arrImage[intRandom];
}
function image_onclick2() {
  var arrImage = new Array("/static/page/img/pedi/pedi1.png", "/static/page/img/pedi/pedi2.png", "/static/page/img/pedi/pedi3.png",
    "/static/page/img/pedi/pedi4.png", "/static/page/img/pedi/pedi5.png", "/static/page/img/pedi/pedi6.png",
    "/static/page/img/pedi/pedi7.png", "/static/page/img/pedi/pedi8.png", "/static/page/img/pedi/pedi9.png",
    "/static/page/img/pedi/pedi10.png", "/static/page/img/pedi/pedi1.png", "/static/page/img/pedi/pedi12.png",
    "/static/page/img/pedi/pedi13.png", "/static/page/img/pedi/pedi14.png", "/static/page/img/pedi/pedi15.png");
  var imgSource = document.targetImg;
  var intRandom = Math.round(Math.random() * 14);
  while (imgSource.src.indexOf(arrImage[intRandom]) != -1) {
    intRandom = Math.round(Math.random() * 14);
  }
  imgSource.src = arrImage[intRandom];
}
