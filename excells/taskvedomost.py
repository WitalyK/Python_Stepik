import xlrd, zipfile, os
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor, as_completed


def completion(name1):
    wb = xlrd.open_workbook('work/' + name1)
    sh = wb.sheet_by_index(0)
    line1 = (sh.row_values(1)[1], sh.row_values(1)[3])
    wb.release_resources()
    return line1


url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
urlretrieve(url, 'work/arhiv.zip')
buh_zip = zipfile.ZipFile('work/arhiv.zip')
buh_zip.extractall('work')
buh_zip.close()
l = [f for f in os.listdir('work') if 'xlsx' in f]
ll = []
with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(completion, name) for name in l]
    for f in as_completed(futures):
        ll.append(f.result())
ll = sorted(ll)
for line in ll:
    print(line[0], int(line[1]))
