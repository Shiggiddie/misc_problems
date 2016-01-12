from django.core.management.base import BaseCommand, CommandError

import json
import requests
import xml.etree.ElementTree as ET

class Command(BaseCommand):
    help = 'Hits the json-endpoint and xml-endpoint and ensures they match, then logs'

    def handle(self, *args, **options):
        # Get score data from JSON endpoint
        json_r = requests.get('http://localhost:8000/json-endpoint')
        try:
            json_data = json_r.json()
        except Exception:
            print('json endpoint had shit data')
        else:
            # Get score data from XML endpoint
            xml_r = requests.get('http://localhost:8000/xml-endpoint')
            tree = ET.ElementTree(ET.fromstring(xml_r.content))

            if tree.getroot().text == str(json_data['score']):
                print('json and tree matched, yay!')
            else:
                print('json value: %r, and tree value: %r, did NOT match, boo!' % (json_data['score'], tree.getroot().text))
