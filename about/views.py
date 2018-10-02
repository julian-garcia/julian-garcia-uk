from django.shortcuts import render
import requests, json, os

def index(request):
    languages = requests.get(os.environ.get('WAKATIME_URL'))
    langs_list = json.loads(languages.content)['data']

    languages_mobile_svg = os.environ.get('WAKATIME_URL_MOBILE')

    langs_dict = {}
    for lang in langs_list:
        langs_dict[lang['name']] = lang['percent']

    return render(request, 'index.html',
                  {'languages': json.dumps(langs_dict),
                   'languages_mobile_svg': languages_mobile_svg})
