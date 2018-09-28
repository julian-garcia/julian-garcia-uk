from django.shortcuts import render
import requests, json

def index(request):
    languages = requests.get('https://wakatime.com/share/@c3419dbf-0038-499d-9d18-532e0b87876f/5936d31f-1414-404c-a67b-98f15a6dbb51.json')
    langs_list = json.loads(languages.content)['data']

    langs_dict = {}
    for lang in langs_list:
        langs_dict[lang['name']] = lang['percent']

    return render(request, 'index.html', {'languages': json.dumps(langs_dict)})
