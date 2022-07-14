# https://docs.djangoproject.com/en/2.0/ref/request-response/
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting"""
    return HttpResponse('Oh, hi! Current time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sorted_ints(request):
    """Sorted ints by params."""
    num_str = request.GET['numbers'].split(',')
    sorted_ints = sorted([int(i) for i in num_str])
    #import pdb; pdb.set_trace()
    return HttpResponse(str(sorted_ints))

def json_ints(request):
    """Sorted json.
    * You can use JSON Viewer extension for Chrome"""
    num_str = request.GET['numbers'].split(',')
    sorted_ints = sorted([int(i) for i in num_str])
    data = {
        'status': 'OK',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
