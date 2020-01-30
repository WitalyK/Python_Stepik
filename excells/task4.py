import xlrd


wb = xlrd.open_workbook('trekking3.xlsx')
shn = wb.sheet_names()
sh1 = wb.sheet_by_name(shn[1])
sh2 = wb.sheet_by_name(shn[0])
d = {}
for row in range(1, sh1.nrows):
    key1 = sh1.row_values(row)[0]
    key = sh1.row_values(row)[1]
    if d.get(key1):
        if d[key1].get(key):
            d[key1][key] += sh1.row_values(row)[2]
        else:
            d[key1][key] = sh1.row_values(row)[2]
    else:
        d[key1] = {key: sh1.row_values(row)[2]}
d2 = {sh2.row_values(row)[0]: [sh2.row_values(row)[1], sh2.row_values(row)[2], sh2.row_values(row)[3],
                               sh2.row_values(row)[4]] for row in range(1, sh2.nrows)}
for key, values in d2.items():
    i = 0
    for val in values:
        if not isinstance(val, float):
            d2[key][i] = 0
        i += 1
for key1, values in d.items():
    a = 0
    b = 0
    c = 0
    d = 0
    for key, val in values.items():
        a += d2[key][0]*val/100
        b += d2[key][1]*val/100
        c += d2[key][2]*val/100
        d += d2[key][3]*val/100
    print(int(a), int(b), int(c), int(d))