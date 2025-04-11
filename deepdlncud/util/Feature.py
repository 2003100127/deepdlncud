__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from rdkit import Chem
from Bio import SeqIO
from deepdlncud.util import Biochar
from deepdlncud.util.Console import Console


def fasta(fasta_fpn):
    sequence = []
    for seq in SeqIO.parse(fasta_fpn, "fasta"):
        # print(seq.seq)
        sequence.append(str(seq.seq))
    sequence = ''.join(sequence)
    if sequence == '':
        print('The sequence is empty.')
    return sequence


def fetch(
        br_fpn,
        smile_fpn,
        fasta_fp,
        verbose=True,
):
    console = Console()
    console.verbose = verbose

    df_br = pd.read_csv(
        br_fpn,
        sep='\t',
        header=0,
    )
    console.print("small-molecule and lncRNA relations:\n{}".format(df_br))
    num_samples = df_br.shape[0]
    df_smile = pd.read_csv(
        smile_fpn,
        sep='\t',
        header=0,
    )
    console.print("small-molecule smile map:\n{}".format(df_smile))
    dict_smile = pd.Series(df_smile['smile'].values, index=df_smile['sm'].values).to_dict()
    # console.print(dict_smile)

    v = [[] for _ in range(num_samples)]
    for i in range(num_samples):
        ntseq = fasta(fasta_fpn=fasta_fp + df_br.loc[i, 'lncrna'] + '.fasta')

        ns_ = Biochar.ns(ntseq)
        ns_ = [*ns_.values()]
        ns_ = [np.float32(i) for i in ns_]
        for j in range(4):
            v[i].append(ns_[j])

        ds_ = Biochar.ds(ntseq)
        ds_ = [*ds_.values()]
        for j in range(16):
            v[i].append(np.float32(ds_[j]))

        ts_ = Biochar.ts(ntseq)
        ts_ = [*ts_.values()]
        for j in range(64):
            v[i].append(np.float32(ts_[j]))

        qs_ = Biochar.qs(ntseq)
        qs_ = [*qs_.values()]
        for j in range(256):
            v[i].append(np.float32(qs_[j]))

        bseqs_ = Biochar.bseqs(ntseq, k=3)
        bseqs_ = [*bseqs_.values()]
        for j in range(16):
            v[i].append(np.float32(bseqs_[j]))

        aseqs_ = Biochar.aseqs(ntseq)
        aseqs_ = [*aseqs_.values()]
        for j in range(4):
            v[i].append(np.float32(aseqs_[j]))


        mol = Chem.MolFromSmiles(dict_smile[df_br.loc[i, 'sm']])
        # print(mol)
        pc10 = Biochar.bcs(mol)
        for _, t in enumerate(pc10):
            v[i].append(np.float32(t))

        pc2 = Biochar.crippen(mol)
        for _, t in enumerate(pc2):
            v[i].append(np.float32(t))

        fp_morgan = Biochar.fp(mol)
        for _, e in enumerate(fp_morgan):
            v[i].append(int(e))
    v = np.array(v)
    return v[:, 0: 1369].astype(np.float32)