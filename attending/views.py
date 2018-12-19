from django.shortcuts import render
from .models import Event
import os, requests, json

def attending(request):
    gmap_api_key = os.environ.get('GMAP_API_KEY')
    gmap_api_url = os.environ.get('GMAP_API_URL')
    coordinates = []
    coord_labels = []

    # Use geocoding to convert the event post code in to coordinates
    # so they can be rendered as markers on the map
    coordinates_request = requests.get('{0}/geocode/json?address=BR20HE&key={1}'.format(gmap_api_url, gmap_api_key))
    coordinates.append(json.loads(coordinates_request.content)['results'][0]['geometry']['location'])
    coord_labels.append('Home')

    events = Event.objects.all().order_by('-event_date')[:5]

    for event in events:
        coordinates_request = requests.get('{0}/geocode/json?address={1}&key={2}'.format(gmap_api_url, event.event_postcode, gmap_api_key))
        coordinates.append(json.loads(coordinates_request.content)['results'][0]['geometry']['location'])
        coord_labels.append(event.event_name)

    return render(request,'attending.html', {'gmap_api_key': gmap_api_key,
                                             'gmap_api_url': gmap_api_url,
                                             'coordinates': coordinates,
                                             'coord_labels': coord_labels,
                                             'events': events})
