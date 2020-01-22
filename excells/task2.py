import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sh = wb.sheet_by_index(0)
l = [sh.row_values(row)[0:2] for row in range(1, sh.nrows)]
l = sorted(l, key=lambda x: (-x[1], x[0]))
for i in l:
    print(i[0])