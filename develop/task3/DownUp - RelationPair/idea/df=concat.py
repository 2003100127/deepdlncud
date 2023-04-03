import pandas as pd
# 读取uptest
# Read uptest
ser1 = pd.read_csv('up_test.txt', sep="\t", header=0,)
print(ser1)

# 读取downtest
# Read downtest
ser2 = pd.read_csv('down_test.txt', sep="\t", header=0,)
print(ser2)

# 用concat让up在上，down在下合并一下
# Use concat to get up on top and down on bottom to merge
print(pd.concat([ser1, ser2], ignore_index=True),)

#打开test,并读取出来
# Open test, and read it out
f = open(r'D:/deepncud-main（2）/deepdlncud/data/result/cnn/test.txt')
ser3 = pd.read_csv(f, sep="\t", header=0,)
# print(ser3)

# 将updown合并后结果和读取出来的test合并
# Combine the updown merge result with the read out test
result = pd.concat([(pd.concat([ser1, ser2], ignore_index=True)), ser3], axis=1, join='inner')
# print(result)
print(result)

# print出来结果行数多中间会有...，这条输入就是为了输出全部显示并存入txt
# print out the result line number more middle will be ...
# This input is for the output to be displayed in full and stored in txt
pd.set_option('display.max_rows', None) # 设置行数显示无限制
result.to_csv('D:/deepncud-main（2）/deepdlncud/data/result/cnn/testresult.txt', sep='\t', index=False)

pd.read_csv('D:/deepncud-main（2）/deepdlncud/data/result/cnn/testresult.txt')
print(pd.read_csv('D:/deepncud-main（2）/deepdlncud/data/result/cnn/testresult.txt', sep='\t'))


