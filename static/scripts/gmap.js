function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: coordinates
  });

  var marker = new google.maps.Marker({
    position: coordinates,
    map: map,
    title: 'Hello World!'
  });
}
