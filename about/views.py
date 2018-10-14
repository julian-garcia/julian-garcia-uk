from django.shortcuts import render
import requests, json, os, math

def index(request):
    languages = requests.get(os.environ.get('WAKATIME_URL'))
    langs_list = json.loads(languages.content)['data']

    langs_dict = {}
    for lang in langs_list:
        langs_dict[lang['name']] = lang['percent']

    languages_mobile_svg = os.environ.get('WAKATIME_URL_MOBILE')

    # Time spent coding to the nearest hour in the last 30 days
    coding_time = requests.get(os.environ.get('WAKATIME_CODING_TIME'))
    coding_list = json.loads(coding_time.content)['data']

    coding_seconds = 0
    for code_activity in coding_list:
        coding_seconds += code_activity['grand_total']['total_seconds']
    coding_hours = math.ceil(coding_seconds / 60 / 60)

    # My meetup groups
    meetups = requests.get('{0}{1}'.format(os.environ.get('MEETUP_API_URL'),os.environ.get('MEETUP_API_KEY')))
    group_list = json.loads(meetups.content)

    meetup_group_list = []
    for group in group_list:
        meetup_group_list.append({'name': group['name'],
                                  'link': group['link'],
                                  'image': group['key_photo']['photo_link']})

    return render(request, 'index.html',
                  {'languages': json.dumps(langs_dict),
                   'languages_mobile_svg': languages_mobile_svg,
                   'coding_hours': coding_hours,
                   'meetup_group_list': sorted(meetup_group_list, key = lambda k: k['name'].upper())})
