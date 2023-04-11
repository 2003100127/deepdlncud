# -*- coding: utf-8 -*-
import pandas as pd
# import python内部功能模块subprocess
import subprocess

#模型名字
# Model name
mets = {
    # 'ResNet18': './resnet18',
    # 'ResNet50': './resnet50',
    'AlexNet': './alexnet/alexnet',
    'BiRNN': './birnn/birnn',
    'RNN': './rnn/rnn',
    'Seq2Seq': './seq2seq/seq2seq',
    'LSTMCNN': './lstmcnn',
    'CNN': './cnn',
    'ConvMixer64': './convmixer64',
    'DSConv': './dsconv',
    'MobileNet': './mobilenet',
    'SEResNet': './seresnet',
}


df = pd.read_csv('D:/deepncud-main（2）/deepdlncud/data/dataset/up_uniq_lncRNAs.txt', sep="\t", header=0,)

print(df.index)
print(df)

# 通过for循环得到模型名字met，相当于每一次for循环都取到模型的名字
# The model name met is obtained by a for loop, which is equivalent to taking the name of the model for each for loop
# 小分子名字也要for循环，顺序读取
# Small molecule names are also read in a for loop, sequentially
for met, met_fp in mets.items():
    for i in df.index:
        # # print(i)
        # print(df.iloc[i][1])
        # print(df.iloc[i][0])

        # print(df.loc[i, 'sm'])
        # print(df.loc[i, 'lncRNA'])
        print(met)
        print('deepsmirud -m ' + met + ' -sm ../data/smc/smile/' + str(
                df.iloc[i][1]) + '.txt -mir ../data/lncrna/fasta/lncipedia/' + str(
                df.iloc[i][0].split(':')[0]) + '.fasta -mf ' + met_fp + ' -o ./' + met + '/' + str(
                df.iloc[i][1]) + '$' + str(df.iloc[i][0].split(':')[0]) + '.deepsmirud',)
        print(df.iloc[i][1])
        print('deepsmirud -m ' + met + ' -sm ../data/smc/smile/' + str(
                df.iloc[i][1]) + '.txt -mir ../data/lncrna/fasta/lncipedia/' + str(
                df.iloc[i][0].split(':')[0]) + '.fasta -mf ' + met_fp + ' -o ./' + met + '/' + str(
                df.iloc[i][1]) + '$' + str(df.iloc[i][0].split(':')[0]) + '.txt',)
        s = subprocess.Popen(
            'deepsmirud -m ' + met + ' -sm ../data/smc/smile/' + str(
                df.iloc[i][1]) + '.txt -mir ../data/lncrna/fasta/lncipedia/' + str(
                df.iloc[i][0].split(':')[0]) + '.fasta -mf ' + met_fp + ' -o ./' + met + '/' + str(
                df.iloc[i][1]) + '$' + str(df.iloc[i][0].split(':')[0]) + '.txt',
            stdout=subprocess.PIPE,
            shell=True,
        )
        s.communicate()
