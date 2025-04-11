# Prediction

## Overview

You need to decompress the `example_data.zip` file in your preferred folder, e.g., `deepdlncud/`.

There are three required files.

* `br_sm_lncrna.txt`
* `br_smile.txt`
* `path` to `*.fasta`

We display 2 pairs of small molecules and lncRNAs to predict their possible regulation types.

```{code}
:linenos:
:emphasize-lines: 2,3

sm	lncrna
6918837	lnc-CPO-4
60606	HIF1A-AS1
```

:::{caution} Model declaration
* Models include `cnn`, `lstmcnn`, `dsconv`, `convmixer64`, `mobilenet`, `resnet_prea18`, `resnet_prea50`, `seresnet`, and `densenet`, you need to declare them like `lstmcnn`.
:::

## Python

We access **DeepdlncUD** by defining the following parameters. 

:::{seealso}
We have `method` defined as **CNN**, **ConvMixer64**, **DSConv**, **LSTMCNN**, **MobileNet**, **ResNet18**, **ResNet50**, **SEResNet**, or **DenseNet**. Please see also the DeepdlncUD paper (@Sun2023deepdlncud) for method details.
:::

```{code} python
params = {
    'br_fpn': '../../data/deepdlncud/example_data/br_sm_lncrna.txt',
    'smile_fpn': '../../data/deepdlncud/example_data/br_smile.txt',
    'fasta_fp': '../../data/deepdlncud/example_data/',
    'method': 'DenseNet',
    'model_fp': '../../data/deepdlncud/model/densenet',
    'sv_fpn': '../../data/deepdlncud/example_data/pred.deepdlncud',
}
```

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import deepdlncud

deepdlncud.predict.sm_lncr_regulation_type(
    br_fpn=params['br_fpn'],
    smile_fpn=params['smile_fpn'],
    fasta_fp=params['fasta_fp'],
    method=params['method'],
    model_fp=params['model_fp'],
    sv_fpn=params['sv_fpn'],
)
```
:::
:::{tab-item} Output log
:sync: tab2
```{code} shell
 ____                      _ _            _   _ ____  
|  _ \  ___  ___ _ __   __| | |_ __   ___| | | |  _ \ 
| | | |/ _ \/ _ \ '_ \ / _` | | '_ \ / __| | | | | | |
| |_| |  __/  __/ |_) | (_| | | | | | (__| |_| | |_| |
|____/ \___|\___| .__/ \__,_|_|_| |_|\___|\___/|____/ 
                |_|                                   

05/04/2025 07:23:03 logger: =>Prediction starts...
05/04/2025 07:23:03 logger: small-molecule and lncRNA relations:
        sm     lncrna
0  6918837  lnc-CPO-4
1    60606  HIF1A-AS1
05/04/2025 07:23:03 logger: small-molecule smile map:
        sm                                              smile
0  6918837  CC1=C(C2=CC=CC=C2N1)CCNCC3=CC=C(C=C3)/C=C/C(=O)NO
1    60606       COC(=O)[C@H](C1=CC=CC=C1Cl)N2CCC3=C(C2)C=CS3
    prob_up     pred_type
0  0.503342  Upregulation
1  0.513831  Upregulation
```
:::
::::


## CLI

DeepdlncUD can also be used in shell. To know how to use, please type

```{code} shell
deepdlncud -h
```

It shows the usage of different parameters.

```{code} shell
-m, --method,
    A deep learning method. It can be any below.
    DenseNet | CNN | ConvMixer64 | DSConv | LSTMCNN |
    MobileNet | ResNet18 | ResNet50 | SEResNet
-br, --br_fpn, binary relations between small molecules and mirnas
-d, --smile_fpn, map between small molecule IDs and their smile strings
-lncr, --fasta_fp, lncRNA fasta file paths
-mf, --model_fp, a model path
-o, --sv_fpn, outputting deepdlncud predictions
```

You can run it using the following code.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deepdlncud -m DenseNet -br ./data/deepdlncud/example_data/br_sm_lncrna.txt -d ./data/deepdlncud/example_data/br_smile.txt -lncr ./data/deepdlncud/example_data/ -mf ./data/deepdlncud/model/densenet -o ./data/deepdlncud/out.deepdlncud
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
 ____                      _ _            _   _ ____
|  _ \  ___  ___ _ __   __| | |_ __   ___| | | |  _ \
| | | |/ _ \/ _ \ '_ \ / _` | | '_ \ / __| | | | | | |
| |_| |  __/  __/ |_) | (_| | | | | | (__| |_| | |_| |
|____/ \___|\___| .__/ \__,_|_|_| |_|\___|\___/|____/
                |_|

05/04/2025 07:59:33 logger: =>Prediction starts...
05/04/2025 07:59:33 logger: small-molecule and lncRNA relations:
        sm     lncrna
0  6918837  lnc-CPO-4
1    60606  HIF1A-AS1
05/04/2025 07:59:33 logger: small-molecule smile map:
        sm                                              smile
0  6918837  CC1=C(C2=CC=CC=C2N1)CCNCC3=CC=C(C=C3)/C=C/C(=O)NO
1    60606       COC(=O)[C@H](C1=CC=CC=C1Cl)N2CCC3=C(C2)C=CS3
[07:59:33] DEPRECATION WARNING: please use MorganGenerator
[07:59:33] DEPRECATION WARNING: please use MorganGenerator
    prob_up     pred_type
0  0.503342  Upregulation
1  0.513831  Upregulation
```
:::
::::