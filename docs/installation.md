# Installation

## Overview

**DeepdlncUD** has been made available to use across different versions of Python and Tensorflow. Given conflicts between dependencies, the following versions are recommended most (please see [log 1](./versions#tbl1) and [log 2](./versions#tbl2)).

  * Python `3.11`
  * Tensorflow `2.14`

## Installing

Then, we can follow the step-by-step precedures for installation.

Step 1: Get the most recent version of **DeepdlncUD** from GitHub (_clone it at your preferred location_), PyPI, or Conda.

```shell
git clone https://github.com/2003100127/deepdlncud.git
```

Step 2: Create a conda environment in your local machine.

```shell
conda create --name deepdlncud python=3.11

conda activate deepdlncud
```

Step 3: install via pip

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```shell
cd deepdlncud

pip install .
```
:::
:::{tab-item} Installation log
:sync: tab2
```{code} shell
Processing d:\document\programming\python\deepdlncud
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: biopython<2.0,>=1.85 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (1.85)
Requirement already satisfied: click<9.0.0,>=8.1.8 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (8.1.8)
Requirement already satisfied: numpy==1.24.3 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (1.24.3)
Requirement already satisfied: pandas<3.0.0,>=2.2.3 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (2.2.3)
Requirement already satisfied: pyfiglet<2.0.0,>=1.0.2 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (1.0.2)
Requirement already satisfied: rdkit<2025.0.0,>=2024.9.6 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (2024.9.6)
Requirement already satisfied: tensorflow==2.14 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (2.14.0)
Requirement already satisfied: tensorflow-io-gcs-filesystem==0.31.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from deepdlncud==0.0.1) (0.31.0)
Requirement already satisfied: tensorflow-intel==2.14.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow==2.14->deepdlncud==0.0.1) (2.14.0)
Requirement already satisfied: absl-py>=1.0.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.2.2)
Requirement already satisfied: astunparse>=1.6.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (1.6.3)
Requirement already satisfied: flatbuffers>=23.5.26 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (25.2.10)
Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.6.0)
Requirement already satisfied: google-pasta>=0.1.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.2.0)
Requirement already satisfied: h5py>=2.9.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.13.0)
Requirement already satisfied: libclang>=13.0.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (18.1.1)
Requirement already satisfied: ml-dtypes==0.2.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.2.0)
Requirement already satisfied: opt-einsum>=2.3.2 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.4.0)
Requirement already satisfied: packaging in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (24.2)
Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (4.25.6)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (78.1.0)
Requirement already satisfied: six>=1.12.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (1.17.0)
Requirement already satisfied: termcolor>=1.1.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.0.1)
Requirement already satisfied: typing-extensions>=3.6.6 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (4.13.1)
Requirement already satisfied: wrapt<1.15,>=1.11.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (1.14.1)
Requirement already satisfied: grpcio<2.0,>=1.24.3 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (1.71.0)
Requirement already satisfied: tensorboard<2.15,>=2.14 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from
tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.14.1)
Requirement already satisfied: tensorflow-estimator<2.15,>=2.14.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.14.0)
Requirement already satisfied: keras<2.15,>=2.14.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.14.0)
Requirement already satisfied: colorama in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from click<9.0.0,>=8.1.8->deepdlncud==0.0.1) (0.4.6)
Requirement already satisfied: python-dateutil>=2.8.2 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from pandas<3.0.0,>=2.2.3->deepdlncud==0.0.1) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from pandas<3.0.0,>=2.2.3->deepdlncud==0.0.1) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from pandas<3.0.0,>=2.2.3->deepdlncud==0.0.1) (2025.2)
Requirement already satisfied: Pillow in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from rdkit<2025.0.0,>=2024.9.6->deepdlncud==0.0.1) (11.1.0)
Requirement already satisfied: wheel<1.0,>=0.23.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from astunparse>=1.6.0->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.45.1)
Requirement already satisfied: google-auth<3,>=1.6.3 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.38.0)
Requirement already satisfied: google-auth-oauthlib<1.1,>=0.5 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (1.0.0)
Requirement already satisfied: markdown>=2.6.8 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.7)
Requirement already satisfied: requests<3,>=2.21.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.32.3)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.1.3)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (5.5.2)
Requirement already satisfied: pyasn1-modules>=0.2.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.4.2)
Requirement already satisfied: rsa<5,>=3.1.4 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (4.9)
Requirement already satisfied: requests-oauthlib>=0.7.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from google-auth-oauthlib<1.1,>=0.5->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.0.0)
Requirement already satisfied: charset-normalizer<4,>=2 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (2025.1.31)
Requirement already satisfied: MarkupSafe>=2.1.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from werkzeug>=1.0.1->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.0.2)
Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (0.6.1)
Requirement already satisfied: oauthlib>=3.0.0 in d:\programming\anaconda3\envs\deepdlncud\lib\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<1.1,>=0.5->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->deepdlncud==0.0.1) (3.2.2)
Building wheels for collected packages: deepdlncud
  Building wheel for deepdlncud (pyproject.toml) ... done
  Created wheel for deepdlncud: filename=deepdlncud-0.0.1-py3-none-any.whl size=8011 sha256=d77bfdd4cbed1f96949dc4fdbcbe52bfca4c0d6d209dd7a900c2418c5d614aba
  Stored in directory: C:\Users\jianf\AppData\Local\Temp\pip-ephem-wheel-cache-wftluoma\wheels\8a\c5\28\f4fe40061f2889b7d495a68dfbc36f76d77998fb68d99b1d61
Successfully built deepdlncud
Installing collected packages: deepdlncud
  Attempting uninstall: deepdlncud
    Found existing installation: deepdlncud 0.0.1
    Uninstalling deepdlncud-0.0.1:
      Successfully uninstalled deepdlncud-0.0.1
Successfully installed deepdlncud-0.0.1
```
:::
::::

Everything should be all set before you run **DeepdlncUD**.