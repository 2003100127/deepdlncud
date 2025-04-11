# Versions

## Change

::::{grid} 2 2 2 2

|   Version   |                                  Date                                   |
|:-----------:|:-----------------------------------------------------------------------:|
| `0.0.0.0.1` |   ![](https://img.shields.io/badge/past_released-March._2023-red.svg)   |
|   `0.0.1`   | ![](https://img.shields.io/badge/latest_released-April._2025-green.svg) |

::::

## Before `0.0.1`

The version `0.0.0.0.1` of **DeepdlncUD** was used to infer a small molecule-lncRNA regulation type per instance only. This process is simplified as follows.

### Small molecule 

> Clopidogrel (CID: 60606)

```shell
COC(=O)[C@H](C1=CC=CC=C1Cl)N2CCC3=C(C2)C=CS3
```

### Target

> HIF1A-AS1

```
>HIF1A-AS1
CGCCGCCGGCGCCCTCCATGGTGAATCGGTCCCCGCGATGTCTTCACGGCGGGCGGCCCCCAGGCTCGCTCCGGCCTAAGCGCTGGCTCCCTCCACACGCGGAGAAGAGAAGGAAAGACTACAGTTCAACTGTCAATTGGTTGATCACCCGGATTTTATCTACACCTTAGCCTATGGTTGTTCATCTCGTCTCTGCCTATGGCCCATTGACTCCCGGATCCCAGCTCCATTCTTCGGTACTTTACGCACCCTGCTTCCAGTACCCCAACCAGAAGAATATATATAGCAGTTAACTGTCAGCTGGCGAAAAGGAGGAAAATTCAGGAAGATAAAATAGCTGAATGAATTATCCCCGCTCCAGAACGCAGAGGAAAAATGAAATGGCCAGACCCAGATGTTAAAAATGTGTTCCTTGCTCTTTCCTGCCCTAGCAAGGGCTGTTCCATGTTTAGGGGATGAATGCCGCTGAGAGTATTAGCAAAAATACATGTGTCATTGAGTCTGAGGAAGATAACTGAGACATACAGGTATTTCTCATAATGCATGTGGGCATCCATAGACATATTCTTAAATGGCTTAAGGACTTGGAAACTACCTCTAGGAAACCTGAAACTTGAATGTTGGTCCACTAGGGAGAAGAAATGTTCCATTA
```

### Inference

```shell
deepdlncud -m LSTMCNN -sm deepdlncud/data/example/60606.txt -lncr deepdlncud/data/example/HIF1A-AS1.fasta -mf /the/path/you/prefer/model/lstmcnn -o ./out.deepdlncud
```


## Tensorflow

::::{caution} Major change in deep learing libraries
In Keras 3, the way to call models becomes completely different from that in Keras 2.

:::{table} The way to use models.
:label: tbl1
:align: center

| Item              | TF Keras 2                 | TF Keras 3                       |
|-------------------|----------------------------|----------------------------------|
| model format      | `.h5` or TF `SavedModel`   | `.keras` (new) + `.h5`  (legacy) |
| `subclass` Models | supported via `SavedModel` | `TFSMLayer` for loading          |

:::

::::

### Comparison

Our experience suggests that changes in Python versions have a smaller impact compared to changes in TensorFlow versions.

:::{table} The way to use models.
:label: tbl2
:align: center

| Python  | Tensorflow verisons        | Supported versions     |
|---------|----------------------------|------------------------|
| `3.11`  | 🌟`2.14`🌟, `2.15`, `2.16` | TF Keras 2, TF Keras 3 |
| `3.12`  | `2.17`, `2.18`, `2.19`     | only TF Keras 3        |

:::