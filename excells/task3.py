import xlrd
from pprint import pprint


wb = xlrd.open_workbook('trekking2.xlsx')
shn = wb.sheet_names()
sh1 = wb.sheet_by_name(shn[1])
sh2 = wb.sheet_by_name(shn[0])
d = {}
for row in range(1, sh1.nrows):
    key = sh1.row_values(row)[0]
    if d.get(key):
        d[key] += sh1.row_values(row)[1]
    else:
        d[key] = sh1.row_values(row)[1]
d2 = {sh2.row_values(row)[0]: [sh2.row_values(row)[1], sh2.row_values(row)[2], sh2.row_values(row)[3],
                               sh2.row_values(row)[4]] for row in range(1, sh2.nrows)}
for key, values in d2.items():
    i = 0
    for val in values:
        if not isinstance(val, float):
            d2[key][i] = 0
        i += 1
list1 = [[d2[key][0]*values/100, d2[key][1]*values/100, d2[key][2]*values/100,
          d2[key][3]*values/100] for key, values in d.items()]
k = 0
b = 0
g = 0
u = 0
for k1, b1, g1, u1 in list1:
    k += k1
    b += b1
    g += g1
    u += u1
k = int(k)
b = int(b)
g = int(g)
u = int(u)
print(k, b, g, u)