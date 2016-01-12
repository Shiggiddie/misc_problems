from django.shortcuts import render
from django.http import HttpResponse

import json
import random
import xml.etree.ElementTree as ET

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def json_endpoint(request):
    state = random.randrange(0,4)
    if state == 0:
        # This is a mock garbage json response
        return HttpResponse('{score:')
    elif state == 1:
        # This is a mock response where score is set such that it will never match XML
        return HttpResponse(json.dumps({"score":random.randrange(10,20)}))
    else:
        # This is a mock response where everything on the json side looks good!
        return HttpResponse(json.dumps({"score":1}))

def xml_endpoint(request):
    state = random.randrange(0,3)
    el = ET.Element('score')
    if state == 0:
        # This is a mock response where score is set such that it will never match JSON
        el.text = str(random.randrange(20,30))
    else:
        # This is a mock response where everything on the json side looks good!
        el.text = '1'
    print(ET.tostring(el))
    return HttpResponse(ET.tostring(el), content_type="application/xhtml+xml")
