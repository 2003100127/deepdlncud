
#这是一个统计一串字符串中各个字符出现的次数,入参一个字符串
#This is a count of the number of occurrences of each character in a string, referenced to a string
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
#This function counts the probability of occurrence of each character in a string, referencing a string
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
    #                     The probability is obtained by dividing the frequency of occurrence by the total length
    return d

#从文件中读取一个字符串出来
#Read a string out of a file
def read_fasta(file):
    with open(file) as f:
        s = f.read()
    s =(s.split('\n'))[1:]#去掉第一行(第一行我通过读取fasta文件名来实现）

    return s[0]

#获取文件夹中所有文件名
#Get all file names in a folder

def get_file_path(path):
    file_list = []
    # root表示正在遍历的文件夹的名字（根/子）；dirs记录正在遍历的文件夹下的子文件夹集合；files记录正在遍历的文件夹中的文件集合
    #root indicates the name of the folder being traversed (root/sub); dirs records the set of subfolders
    # under the folder being traversed; files records the set of files in the folder being traversed
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))# 递归获取路径下所有文件名
    return file_list

#格式化输出
#Formatted output
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
#Save data append to a csv file
def save_to_csv(string):
    with open('result.csv','a') as f:
        f.write(string)


#从file_list中顺序读取文件名,并统计每个文件中各个字符出现的概率
#Read the file names sequentially from file_list and count the probability of each character occurring in each file
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

#通过pandas 计算result.csv 中 T C A G 列的平均值
#Calculate the average of the T C A G columns in result.csv via pandas
import pandas as pd

#读取result.csv文件
#Read the result.csv file
data_table = pd.read_csv('result.csv')

# 均值作图
# Means plotting
# 计算T C A G 列的平均值
# Calculate the mean of the T C A G column
print(data_table.mean(axis=0))

#计算T C A G 列的平均值
# Calculate the mean of the T C A G column
T_mean = data_table['T'].mean()
print('T_mean = ',T_mean)
C_mean = data_table['C'].mean()
print('C_mean = ',C_mean)
A_mean = data_table['A'].mean()
print('A_mean = ',A_mean)
G_mean = data_table['G'].mean()
print('G_mean = ',G_mean)

# 利用matplotlib生成图表
# Generating diagrams with matplotlib
x_pos = [0, 1, 2, 3] # 生成数值形成坐标
plt.bar(
    x_pos,
    data_table.mean(axis=0),
    color = 'mediumslateblue',
    width = 0.4,# 条柱的宽
    alpha = 0.6,# 颜色透明度
)
plt.ylabel('Frequency')
plt.xticks(x_pos,['T', 'C', 'A', 'G'])
plt.show()




#这是一个统计一串字符串中各个字符出现的次数,入参一个字符串
# This is a count of the number of occurrences of each character in a string, referenced to a string
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
# This function counts the probability of occurrence of each character in a string, referencing a string
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
#Read a string out of a file
def read_fasta(file):
    with open(file) as f:
        s = f.read()
    s =(s.split('\n'))[1:]#去掉第一行(第一行我通过读取fasta文件名来实现）

    return s[0]

#获取文件夹中所有文件名
# Get all file names in a folder
def get_file_path(path):
    file_list = []
    # root表示正在遍历的文件夹的名字（根/子）；dirs记录正在遍历的文件夹下的子文件夹集合；files记录正在遍历的文件夹中的文件集合
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))# 递归获取路径下所有文件名
    return file_list

#格式化输出
# Formatted output
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
# Save data append to a csv file
def save_to_csv(string):
    with open('result.csv','a') as f:
        f.write(string)


#从file_list中顺序读取文件名,并统计每个文件中各个字符出现的概率
# Read the file names sequentially from file_list and count the probability of each character occurring in each file
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

#通过pandas 计算result.csv 中 T C A G 列的平均值
# Calculate the average of the T C A G columns in result.csv via pandas
import pandas as pd

#读取result.csv文件
# Read the result.csv file
data_table = pd.read_csv('result.csv')

# 均值作图
# Means plotting
# 计算T C A G 列的平均值
# Calculate the mean of the T C A G column
print(data_table.mean(axis=0))
#计算T C A G 列的平均值
# Calculate the mean of the T C A G column
T_mean = data_table['T'].mean()
print('T_mean = ',T_mean)
C_mean = data_table['C'].mean()
print('C_mean = ',C_mean)
A_mean = data_table['A'].mean()
print('A_mean = ',A_mean)
G_mean = data_table['G'].mean()
print('G_mean = ',G_mean)

# 利用matplotlib生成图表
# Generating diagrams with matplotlib
x_pos = [0, 1, 2, 3] # 生成数值形成坐标
plt.bar(
    x_pos,
    data_table.mean(axis=0),
    color = 'mediumslateblue',
    width = 0.4,# 条柱的宽
    alpha = 0.6,# 颜色透明度
)
plt.ylabel('Frequency')
plt.xticks(x_pos,['T', 'C', 'A', 'G'])
plt.show()






