var map, heatmap;

function get_markers(map){  


var marker1 = new google.maps.Marker({
    position: 
                {lat: 28.525507, lng: 77.1840862 },
            
    map: map,
    title: 'ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM'
  });



var marker2 = new google.maps.Marker({
    position: 
                {lat: 28.6923729, lng: 76.9954194 },
            
    map: map,
    title: 'ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM'
  });


var marker3 = new google.maps.Marker({
    position: 
                {lat: 28.5471945, lng: 77.0374669 },
            
    map: map,
    title: 'ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM'
  });
     

var marker4 = new google.maps.Marker({
    position: 
                {lat: 19.1070845, lng: 72.8821504 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Andheri (E), Mumbai, Maharashtra'
  });

var marker5 = new google.maps.Marker({
    position: 
                {lat: 18.9333571, lng: 72.8314793 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Fort, Mumbai'
  });


var marker6 = new google.maps.Marker({
    position: 
                {lat: 19.1862033, lng: 72.8276892 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Malad, Mumbai'
  });



var marker7 = new google.maps.Marker({
    position: 
                {lat: 19.0163602, lng: 72.8249249 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Prabhadevi, Mumbai'
  });


var marker8 = new google.maps.Marker({
    position: 
                {lat: 19.0495536, lng: 72.8747062 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Sion, Mumbai'
  });


var marker9 = new google.maps.Marker({
    position: 
                {lat: 19.1164241, lng: 72.8484543 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Teli gali, Mumbai'
  });


var marker10 = new google.maps.Marker({
    position: 
                {lat: 19.2038274, lng: 72.9752509 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Thane, Mumbai'
  });

var marker11 = new google.maps.Marker({
    position: 
                {lat: 19.0644061, lng: 72.9946395 },
            
    map: map,
    title: 'ICICI Lombard General Insurance Co. Ltd, Vashi , Mumbai'
  });


return [marker11, marker10, marker9, marker8, marker7, marker6, marker5, marker4, marker3, marker2, marker1]
}

      function initMap() {
        document.getElementById('mapCase').style.height="313px";
        document.getElementById('mapCase').style.width="508px";

        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 23,
          center: 
                {lat: 19.0495536, lng: 72.8747062},
          mapTypeId: 'satellite'
        });


map.markers = get_markers();


var i = 0;

  var start = {lat: 0, lng: 0 };
  var end = {lat: 0, lng: 0 };

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }





      }

















function rad(x) {return x*Math.PI/180;}
var f = 0;
function find_closest_marker(lat, lng  ) {
    var R = 6371; // radius of earth in km
    var distances = [];
    var closest = -1;
    for( i=0;i<map.markers.length; i++ ) {
        var mlat = map.markers[i].position.lat();
        var mlng = map.markers[i].position.lng();
        var dLat  = rad(mlat - lat);
        var dLong = rad(mlng - lng);
        var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(rad(lat)) * Math.cos(rad(lat)) * Math.sin(dLong/2) * Math.sin(dLong/2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        var d = R * c;
        distances[i] = d;
        if ( closest == -1 || d < distances[closest] ) {
            closest = i;
        }
    }


return map.markers[closest].title

}













function calcRoute( directionsService, directionsDisplay, start, end) {
  var selectedMode = document.getElementById('mode').value;
  // Note that Javascript allows us to access the constant
          // using square brackets and a string value as its
          // "property."
          
          var selectedMode = document.getElementById('mode').value;


  var request = {
    origin: start,
    destination: end,
    travelMode: google.maps.TravelMode[selectedMode]
  };

  directionsService.route(request, function(result, status) {
    if (status == 'OK') {
      directionsDisplay.setDirections(result);
    }
    else{
      console.log("Direction status",status)
    }
  });
}






function showPosition(position) {
start = { lat : position.coords.latitude, lng : position.coords.longitude}
f = find_closest_marker( lat = position.coords.latitude, lng = position.coords.longitude );

console.log("lat"+ start.lat + "long" + f);



for (var i = map.markers.length - 1; i >= 0; i--) {
  if(f == map.markers[i].title)
  {
      end = map.markers[i].position;
    }
  }


  var directionsDisplay = new google.maps.DirectionsRenderer();
  
  


  directionsDisplay.setMap(map);
         var directionsService = new google.maps.DirectionsService();

calcRoute(directionsService, directionsDisplay, start, end)

document.getElementById('mode').addEventListener('change', function() {
          calcRoute(directionsService, directionsDisplay, start, end );
        });
      }


function CurrentLatLng(position) {
$('body').attr("lat", position.coords.latitude) ;
$('body').attr("lng", position.coords.longitude)  ;

}

function dyna(){
$('tr[name^=garage_select_]').click(function(){
$('tr[name^=garage_select_]').css("background-color", "");

console.log("$(this).lat,  $(this).lng",$(this).attr('lat'),$(this).attr('lng') )
  var directionsDisplay = new google.maps.DirectionsRenderer();

  markers = get_markers(map);

directionsDisplay.setMap(null);
directionsDisplay = null;
    directionsDisplay.setMap(map);
         var directionsService = new google.maps.DirectionsService();

        navigator.geolocation.getCurrentPosition(CurrentLatLng);
console.log("{lat: $(this).attr('lat'), lng: $(this).attr('lng')}",{lat: $(this).attr('lat'), lng: $(this).attr('lng')});
console.log("{lat: $('body').attr('lat'), lng: $('body').attr('lng')}",
  end={"lat": parseFloat($("body").attr('lat').slice(0, 8)), "lng": parseFloat($("body").attr('lng').slice(0, 8))});
calcRoute(directionsService=directionsService, directionsDisplay=directionsDisplay, 
  start={"lat": parseFloat($(this).attr('lat').slice(0, 8)), "lng": parseFloat($(this).attr('lng').slice(0, 8))},
  end={"lat": parseFloat($("body").attr('lat').slice(0, 8)), "lng": parseFloat($("body").attr('lng').slice(0, 8))}  )
});
}


function find_closest(position) {
console.log("at find_closest(position)",e["context"].id);
for (var i = 4 - 1; i >= 0; i--) {
$("tbody"+ ":nth-child("+i+")").text(find_closest_marker( lat = position.coords.latitude, lng = position.coords.longitude ));
}

}
