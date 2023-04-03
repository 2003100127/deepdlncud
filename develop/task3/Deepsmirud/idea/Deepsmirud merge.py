import pandas as pd

# 将down test里每个pair的lncRNA名字按顺序读取出来
# Read out the lncRNA names of each pair in the down test in order
df = pd.read_csv('D:/deepncud-main（2）/deepdlncud/data/dataset/up_uniq_lncRNAs.txt', sep="\t", header=0,)
df_combi = pd.DataFrame()

for i in df.index:
    # 利用loc和iloc索引
    # Using loc and iloc indexes
    lncrna_i = df.loc[i, 'lncRNA']
    sm_i = df.loc[i, 'sm']
    # sm + $ + lncrna = filename
    df_indiv = pd.read_csv(
        'D:/deepncud-main（2）/deepdlncud/dti/seresnet/up_uniq_lncRNAs result/' + str(sm_i) + '$' + str(lncrna_i) + '.txt',
        sep='\t')
    # print(df_indiv)

    # 空数据框和indiv合并是indiv
    # Empty data boxes and indiv merged are indiv
    df_combi = pd.concat([df_combi, df_indiv], axis=0)
    # print(df_indiv)
print(df_combi)

#保证行序列是从1往下依次写，而不是所有行序列都是0
# Ensure that line sequences are written in order from 1 downwards and not all lines are 0
df_combi = df_combi.reset_index(drop=True)
print(df_combi)

# 输出到excel里
# Export to excel
df_combi.to_excel('D:/deepncud-main（2）/deepdlncud/dti/seresnet/up_uniq_lncRNAs result.xlsx')

# 合并up result 和down result到result中
# 合并向上的结果和向下的结果到结果中
import pandas as pd
ser1 = pd.read_excel('D:/deepncud-main（2）/Four tasks/task3/Deepsmirud/PrintResult/seresnet/test result/uptest result.xlsx', header=0,)
ser2 = pd.read_excel('D:/deepncud-main（2）/Four tasks/task3/Deepsmirud/PrintResult/seresnet/test result/downtest result.xlsx', header=0,)
df_combi = pd.concat([ser1, ser2],axis=0)
df_combi = df_combi.reset_index(drop=True)
print(df_combi)

df_combi.to_excel('D:/deepncud-main（2）/Four tasks/task3/Deepsmirud/PrintResult/seresnet/test result/test result.xlsx')