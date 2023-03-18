__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from rdkit import Chem
from deepdlncud.Utils import fasta
from deepdlncud import Biochar


def fetch(
        smile_fpn,
        fasta_fpn,
):
    smile = pd.read_csv(
        smile_fpn,
        sep='\t',
        header=None,
    )
    print(smile)
    mol = Chem.MolFromSmiles(smile.loc[0, 0])
    print(mol)
    v = [[] for _ in range(1)]

    ntseq = fasta(fasta_fpn=fasta_fpn)

    ns_ = Biochar.ns(ntseq)
    ns_ = [*ns_.values()]
    ns_ = [np.float32(i) for i in ns_]
    for j in range(4):
        v[0].append(ns_[j])

    ds_ = Biochar.ds(ntseq)
    ds_ = [*ds_.values()]
    for j in range(16):
        v[0].append(np.float32(ds_[j]))

    ts_ = Biochar.ts(ntseq)
    ts_ = [*ts_.values()]
    for j in range(64):
        v[0].append(np.float32(ts_[j]))

    qs_ = Biochar.qs(ntseq)
    qs_ = [*qs_.values()]
    for j in range(256):
        v[0].append(np.float32(qs_[j]))

    bseqs_ = Biochar.bseqs(ntseq, k=3)
    bseqs_ = [*bseqs_.values()]
    for j in range(16):
        v[0].append(np.float32(bseqs_[j]))

    aseqs_ = Biochar.aseqs(ntseq)
    aseqs_ = [*aseqs_.values()]
    for j in range(4):
        v[0].append(np.float32(aseqs_[j]))

    pc10 = Biochar.bcs(mol)
    for _, t in enumerate(pc10):
        v[0].append(np.float32(t))

    pc2 = Biochar.crippen(mol)
    for _, t in enumerate(pc2):
        v[0].append(np.float32(t))

    fp_morgan = Biochar.fp(mol)
    for _, e in enumerate(fp_morgan):
        v[0].append(np.int(e))
    v = np.array(v)
    return v[:, 0: 1369].astype(np.float32)