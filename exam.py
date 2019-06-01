import xlrd
import random
wb = xlrd.open_workbook('vocabulary.xlsx')
sh = wb.sheets()[0]
col1 = sh.col_values(1)
col2= sh.col_values(2)
dic = dict(zip(col1, col2))

keys = random.sample(list(dic), 10)
print(keys)


