import requests
import json

import urllib.parse

text = input('ASCII Art Text > ')
text = urllib.parse.quote(text)
font = input('ASCII Art Font > ')

# http://artii.herokuapp.com/fonts_list

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)
