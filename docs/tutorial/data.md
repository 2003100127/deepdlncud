# Data

## Small molecule-lncRNA pairs

There are 2 small molecule-lncRNA (SM-lncRNA) pairs as follows.

| No. | small molecule |   lncrna  |
|:---:|:--------------:|:---------:|
|  1  |    6918837     | lnc-CPO-4 |
|  2  |     60606      | HIF1A-AS1 |


## LncRNAs

:::{note} Fasta
:class: dropdown
Protein sequences in [the Fasta format](https://en.wikipedia.org/wiki/FASTA_format) are required. The file extension must be `.fasta` for recognition of the software.
:::

## Small molecules

Drutai reads the smile strings of small molecules as follows. This needs to be separated by `tab`.

| No. | small molecule |             smile             |
|:---:|:--------------:|:-----------------------------:|
|  1  |    6918837     |  CC1=C(C2=CC=C...C=C/C(=O)NO  |
|  2  |    60606       | COC(=O)[C@H](...C3=C(C2)C=CS3 |


## Example data

Users can download our example data this way.

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deepdlncud

deepdlncud.predict.download_data(
    url='https://github.com/2003100127/deepdlncud/releases/download/example-data/example_data.zip',
    sv_fpn='../../data/deepdlncud/example_data.zip',
)
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

05/04/2025 07:08:20 logger: downloading data...
05/04/2025 07:08:21 logger: downloaded!
```
:::
::::

