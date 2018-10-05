from django.shortcuts import render
import os, requests, json

def attending(request):
    gmap_api_key = os.environ.get('GMAP_API_KEY')
    gmap_api_url = os.environ.get('GMAP_API_URL')
    coordinates_request = requests.get('{0}/geocode/json?address=BR20HE&key={1}'.format(gmap_api_url, gmap_api_key))
    coordinates = json.loads(coordinates_request.content)['results'][0]['geometry']['location']

    return render(request,'attending.html', {'gmap_api_key': gmap_api_key, 
                                             'gmap_api_url': gmap_api_url,
                                             'coordinates': coordinates})
