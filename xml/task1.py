from urllib.request import urlretrieve
import xmltodict, requests

url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
urlretrieve(url, 'map1.osm')
with open('map1.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()

# res = requests.get('https://stepik.org/media/attachments/lesson/245571/map1.osm')
# xml = res.text

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])