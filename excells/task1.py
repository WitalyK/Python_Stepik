import xlrd
import numpy


wb = xlrd.open_workbook('salaries.xlsx')
sh = wb.sheet_by_index(0)
d = {}
for row in range(1, sh.nrows):
    l = sh.row_values(row)
    d[sorted(l[1:])[3]] = l[0]
print(d[sorted(list(d.keys()), reverse=True)[0]])

d = {}
for col in range(1, sh.ncols):
    l = sh.col_values(col)
    d[numpy.mean(l[1:])] = l[0]
print(d[sorted(list(d.keys()), reverse=True)[0]])
