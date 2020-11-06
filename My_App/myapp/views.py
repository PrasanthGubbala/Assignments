from django.shortcuts import render
import json
from django.http import HttpResponse

def main(request):
    return render(request,'main.html')

def links(request):
    dict = {
        'image': 'https://avatars1.githubusercontent.com/u/35547667?s=400&amp',
        'linkedin':'https://www.linkedin.com/in/bbeklinker',
        'github':'https://github.com/bbekgit',
        'portfolio':'https://bibekgupta.com/',
        'hacker_rank':'https://www.hackerrank.com/bbekgupta',
        'let_code':'https://leetcode.com/bbekgupta/',
        'twitter':'https://twitter.com/bbektwit?lang=en',
        'facebook':'https://www.facebook.com/Bibekbabu7/',
    }
    json_data = json.dumps(dict)
    return HttpResponse(json_data,content_type='Application/json')