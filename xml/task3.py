from urllib.request import urlretrieve
import xmltodict, requests
from pprint import pprint

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
urlretrieve(url, 'map2.osm')
with open('map2.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()

# res = requests.get('https://stepik.org/media/attachments/lesson/245571/map1.osm')
# xml = res.text
withfuel = 0
parsedxml = xmltodict.parse(xml)
for item in parsedxml['osm']['node']:
    if 'tag' in item:
        tags = item['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == "amenity" and tag['@v'] == "fuel":
                    withfuel += 1
        else:
            if '@k' in tags and tags['@k'] == "amenity" and tags['@v'] == "fuel":
                withfuel += 1
print(withfuel)
#pprint(parsedxml['osm']['node'])
# parsedxml['osm']['node'][100]['@id']
#  https://stepik.org/media/attachments/lesson/245678/map1.osm
# "<tag k="amenity" v="fuel"/>"