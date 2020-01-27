from urllib.request import urlretrieve
import xmltodict, requests
from pprint import pprint

url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
urlretrieve(url, 'map1.osm')
with open('map1.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()

# res = requests.get('https://stepik.org/media/attachments/lesson/245571/map1.osm')
# xml = res.text
withtag = 0
withouttag = 0
parsedxml = xmltodict.parse(xml)
for item in parsedxml['osm']['node']:
    if 'tag' in item:
        withtag += 1
    else:
        withouttag += 1
print(withtag, withouttag)
#pprint(parsedxml['osm']['node'])
# parsedxml['osm']['node'][100]['@id']
#  https://stepik.org/media/attachments/lesson/245678/map1.osm
"сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа, разделённых пробелом"