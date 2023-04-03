import pandas as pd
#读取data.xlsx表中的数据
# Read data from the data.xlsx table
data = pd.read_excel("D:/deepncud-main（2）/deepdlncud/data/dz/LncRNADisease/experimental lncRNA-disease information.xlsx")

#读取found.xlsx表中的数据
# Read the data in the found.xlsx table
found = pd.read_excel("D:/deepncud-main（2）/deepdlncud/found.xlsx")

#将两个表格ncRNA Symbol进行合并，保留found表中所有的对象,并为重复的列指定不同的后缀
# Merge the two tables ncRNA Symbol, keeping all the objects
# in the found table and assigning different suffixes to the duplicate columns
merged = pd.merge(
    found,
    data,
    on="ncRNA Symbol",
    how="inner",
    suffixes=("_found","_data")
)

#去重
# de-weighting
# merged = merged.drop_duplicates(subset=["ncRNA Symbol"], keep='first')

#筛选出found表中原有的对象
# Filter out the original objects in the found table
merged = merged[merged["ncRNA Symbol"].isin(found["ncRNA Symbol"])]
print(merged)
#排列一下
# Arrange it
merged = merged.sort_values(by="ncRNA Category", ascending=False)

#将结果保存到result.xlsx中
# Save the results to result.xlsx
merged.to_excel("D:/deepncud-main（2）/deepdlncud/result.xlsx", index=False)