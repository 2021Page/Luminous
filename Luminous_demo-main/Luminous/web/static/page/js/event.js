
language = "JavaScript"
google.charts.load('current', {packages: ['corechart']});
function drawChart() {
// Define the chart to be drawn.
 var data = google.visualization.arrayToDataTable([
   ['Event Name', 'Participation Rate'],
   ['New Member Event',  80,],
   ['Ruminous SNS Event',  45],
   ['Ruminous Kakao Channel Addition Event',  30]

]);

var options = {title: 'Percentage of participation in events to members ( 100% )'};

// Instantiate and draw the chart.
var chart = new google.visualization.BarChart(document.getElementById('container'));
chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);
