import pandas as pd
import xlsxwriter

array = [['a1', 'a2', 'a3'],
         ['a4', 'a5', 'a6'],
         ['a7', 'a8', 'a9'],
         ['a10', 'a11', 'a12', 'a13', 'a14']]

months = ['jan', 'feb', 'mar', 'apr', 'may']
df = pd.DataFrame(array, columns=months)

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Тест1', header=True, index=False)
df.to_excel(writer, sheet_name='Тест2', header=False, index=False)
df.to_excel(writer, sheet_name='Тест3', header=False, index=False)

writer.save()