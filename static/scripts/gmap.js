function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: {lat: 51.515069, lng: -0.1107947},
    mapTypeControl: false
  });

  let i = 0;
  coordinates.forEach(function(coordinate) {
    var marker = new google.maps.Marker({
      position: coordinate,
      map: map,
      title: coord_labels[i]
    });
    i += 1;
  });
}
