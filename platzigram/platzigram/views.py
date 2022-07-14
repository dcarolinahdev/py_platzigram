# https://docs.djangoproject.com/en/2.0/ref/request-response/
# Django
from email import message
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting"""
    return HttpResponse('Oh, hi! Current time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def say_hi(request, name, age):
    """Return a greeting with name"""
    if age < 15:
        message = 'Sorry {}, you are not allowed here :('.format(name)
    else:
        message = 'Hi {}! Welcome to Platzigram :)'.format(name)
    return HttpResponse(message)

def sorted_ints(request):
    """Sorted ints by params."""
    num_str = request.GET['numbers'].split(',')
    sorted_ints = sorted([int(i) for i in num_str])
    #import pdb; pdb.set_trace()
    return HttpResponse(str(sorted_ints))

def json_ints(request):
    """Return a JSON response with sorted integers.
    * You can use JSON Viewer extension for Chrome"""
    num_str = request.GET['numbers'].split(',')
    sorted_ints = sorted([int(i) for i in num_str])
    data = {
        'status': 'OK',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
