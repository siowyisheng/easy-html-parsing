# Parsing an HTML from URL

from lxml import html
import requests

URL = 'https://sherlock-holm.es/stories/pdf/a4/1-sided/')
r = requests.get(URL)
tree = html.fromstring(r.content)
paths = tree.xpath('//a/text()')
root_path = 'https://sherlock-holm.es/stories/pdf/a4/1-sided/'

for path in paths:
    r = requests.get(root_path + path)
    with open(path, 'wb') as f:
        f.write(r.content)