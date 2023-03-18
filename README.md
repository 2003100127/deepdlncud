# DeepdlncUD
![](https://img.shields.io/badge/deepdlncud-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released-June._2022-green.svg)
![](https://img.shields.io/github/stars/2003100127/deepdlncud?logo=GitHub&color=blue)
![](https://img.shields.io/pypi/v/deepdlncud?logo=PyPI)
[![Downloads](https://pepy.tech/badge/deepdlncud)](https://pepy.tech/project/deepdlncud)
[![Downloads](https://pepy.tech/badge/deepdlncud/month)](https://pepy.tech/project/deepdlncud)
[![Downloads](https://pepy.tech/badge/deepdlncud/week)](https://pepy.tech/project/deepdlncud)

###### tags: `lncRNA` `drugs` `gene regulation`

## Overview
```angular2html
 ____                      _ _            _   _ ____
|  _ \  ___  ___ _ __   __| | |_ __   ___| | | |  _ \
| | | |/ _ \/ _ \ '_ \ / _` | | '_ \ / __| | | | | | |
| |_| |  __/  __/ |_) | (_| | | | | | (__| |_| | |_| |
|____/ \___|\___| .__/ \__,_|_|_| |_|\___|\___/|____/
                |_|
```
This repository is a standalone package of the DeepdlncUD method. DeepdlncUD is used to predict the regulation types of small molecules on modulating lncRNA expression. This method is powered by 9 deep learning models.

## Installation
* ### PyPI
```angular2html
pip install deepdlncud
```

## Overview
```angular2html
deepdlncud [-h]
           --method m
           --smile_fpn sm
           --fasta_fpn lncr
           --model_fp mf
           --output_path o

argument details:
    -h, --help            show this help message and exit
    -m, --method,
            A deep learning method. It can be any below.
            DenseNet18 | CNN | ConvMixer64 | DSConv | LSTMCNN | MobileNet | ResNet18 | ResNet50 | SEResNet


    -sm, --smile_fpn, a small molecule file that contains only smile strings


    -lncr, --fasta_fpn, a lncRNA fasta file


    -mf, --model_fp, a model path


    -o, --output_path, outputting deepdlncud predictions
```

## Usage
### Download models
```shell
deepdlncud_download -o /the/path/you/prefer/model.zip
```

```
# output messages
downloading...
downloaded!
```
Please use `-mf` of `deepdlncud` then to access to where the models are located.

### Input format
Two example files in DeepdlncUD are 60606.txt and HIF1A-AS1.fasta for a small molecule and a lncRNA molecule.

* #### Clopidogrel (small molecule CID: 60606)

![estradiol](https://github.com/2003100127/deepdlncud/blob/main/img/Clopidogrel.png?raw=true)
```shell
# 60606.txt
C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=C3C=CC(=C4)O
```

* #### hsa-let-7e-5p (lncRNA)
```
# HIF1A-AS1.fasta
>HIF1A-AS1
CGCCGCCGGCGCCCTCCATGGTGAATCGGTCCCCGCGATGTCTTCACGGCGGGCGGCCCCCAGGCTCGCTCCGGCCTAAGCGCTGGCTCCCTCCACACGCGGAGAAGAGAAGGAAAGACTACAGTTCAACTGTCAATTGGTTGATCACCCGGATTTTATCTACACCTTAGCCTATGGTTGTTCATCTCGTCTCTGCCTATGGCCCATTGACTCCCGGATCCCAGCTCCATTCTTCGGTACTTTACGCACCCTGCTTCCAGTACCCCAACCAGAAGAATATATATAGCAGTTAACTGTCAGCTGGCGAAAAGGAGGAAAATTCAGGAAGATAAAATAGCTGAATGAATTATCCCCGCTCCAGAACGCAGAGGAAAAATGAAATGGCCAGACCCAGATGTTAAAAATGTGTTCCTTGCTCTTTCCTGCCCTAGCAAGGGCTGTTCCATGTTTAGGGGATGAATGCCGCTGAGAGTATTAGCAAAAATACATGTGTCATTGAGTCTGAGGAAGATAACTGAGACATACAGGTATTTCTCATAATGCATGTGGGCATCCATAGACATATTCTTAAATGGCTTAAGGACTTGGAAACTACCTCTAGGAAACCTGAAACTTGAATGTTGGTCCACTAGGGAGAAGAAATGTTCCATTA
```

### Inference
Use two example files in DeepdlncUD. The ConvMixer64 model is recommanded to use in your studies.
```shell
deepdlncud -m LSTMCNN -sm deepdlncud/data/example/60606.txt -lncr deepdlncud/data/example/HIF1A-AS1.fasta -mf /the/path/you/prefer/model/lstmcnn -o ./out.deepdlncud
```

## Citation
Please cite our work if you use DeepdlncUD in your research.

## Contact
If you have any question, please contact [Jianfeng Sun](jianfeng.sunmt@gmail.com). We highly recommend creating issue pages when you have problems. Your issues will be responded then.

