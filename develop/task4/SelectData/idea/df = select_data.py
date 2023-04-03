# -*- coding: utf-8 -*-

import pandas as pd
# （1）第十一列除up和down外都去除掉  （2）第八列除了homo sapiens外都去除掉
# (1) Column 11 removed except for up and down (2) Column 8 removed except for homo sapiens
# 读取excel表格数据
# Read excel spreadsheet data
df = pd.read_excel('D:/deepncud-main（2）/deepdlncud/data_select/result.xlsx')
print(df)

# 利用isin()函数接受列表，判断指定列中指定元素是否在列表中，同时多个列进行过滤
# Use the isin() function to accept a list, determine if a specified element in a specified column is in the list,
# and filter on multiple columns at the same time
df = df[df['Dysfunction Pattern'].isin(['Regulation [up-regulated]','Regulation [down-regulated]'])
        & df['Species'].isin(['Homo sapiens', ])]
print(df)

# 保存为新的Excel
# Save as new Excel
df.to_excel('D:/deepncud-main（2）/deepdlncud/data_select/result2.xlsx')

# 第六列和第十一列综合起来筛选来实现对药物的筛选
# The sixth and eleventh columns are combined to screen for drugs
# 组合筛选
# Portfolio screening
outfile = df.loc[(df['reg.1']== 1)]
outfile1 = outfile.loc[(outfile['Dysfunction Pattern']=='Regulation [down-regulated]')]

outfile2 = df.loc[(df['reg']== 1)]
outfile3 = outfile2.loc[(outfile2['Dysfunction Pattern']=='Regulation [up-regulated]')]
print(outfile3)
result = pd.concat([outfile1, outfile3],axis=0).reset_index(drop=True)

# 保存为新的Excel
# Save as new Excel
result.to_excel('D:/deepncud-main（2）/deepdlncud/data_select/outfile.xlsx')


