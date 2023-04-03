#这是一个统计一串字符串中各个字符出现的次数,入参一个字符串
import os
import pandas as pd
from matplotlib import pyplot as plt, ticker


def count(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

#这个函数统计一串字符串中各个字符出现的概率,入参一个字符串
def count_prob(s):
    d = {}
    for i in s:
        if i == '' :
            continue
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        d[i] = d[i]/len(s) # 出现频数除以总长度就可以得到概率
    return d

#从文件中读取一个字符串出来
def read_fasta(file):
    with open(file) as f:
        s = f.read()
    s =(s.split('\n'))[1:]#去掉第一行(第一行我通过读取fasta文件名来实现）

    return s[0]

#获取文件夹中所有文件名
def get_file_path(path):
    file_list = []
    # root表示正在遍历的文件夹的名字（根/子）；dirs记录正在遍历的文件夹下的子文件夹集合；files记录正在遍历的文件夹中的文件集合
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))# 递归获取路径下所有文件名
    return file_list

#格式化输出
def print_dict(file_name,d):
    file_name = file_name.replace('lncipedia','')       #去掉文件名中的lncipedia
    file_name = file_name.replace('.','')               #去掉文件名中的.
    file_name = file_name.replace('\\','')              #去掉文件名中的\
    file_name = file_name.replace('fasta','')           #去掉文件名中的fasta
    print(file_name,end='\t\t')
    print("{:.6f}\t".format(d['T']),end='')
    print("{:.6f}\t".format(d['C']),end='')
    print("{:.6f}\t".format(d['A']),end='')
    print("{:.6f}\t".format(d['G']),)



#将数据追加保存到csv文件中
def save_to_csv(string):
    with open('result.csv','a') as f:
        f.write(string)


#从file_list中顺序读取文件名,并统计每个文件中各个字符出现的概率
save_to_csv("name,T,C,A,G\n")
file_list = get_file_path('.\lncipedia')

for file_name in file_list:
    string = read_fasta(file_name)
    data =count_prob(string)
    print_dict(file_name,data)
    file_name = file_name.replace('lncipedia','')
    file_name = file_name.replace('.','')
    file_name = file_name.replace('\\','')
    file_name = file_name.replace('fasta','')

    save_to_csv(file_name+str(',')
                +str("{:.6f}".format(data['T']))+str(',')
                +str("{:.6f}".format(data['T']))+str(',')
                +str("{:.6f}".format(data['T']))+str(',')
                +str("{:.6f}".format(data['T']))+str('\n'))




#
#
# ......
# 进行画图主体部分
# ......

# 第一组散点
import matplotlib.pyplot as plt
# 读入
df = pd.read_csv('result.csv')


# s 点的大小  c 点的颜色 alpha 透明度
plt.scatter(x=df['name'], y=df['T'], s=10, c='mediumslateblue', alpha=0.5)


# 设置 x 坐标轴标签的显示内容和大小


plt.ylabel("Frequency")

# 出图
plt.show()





