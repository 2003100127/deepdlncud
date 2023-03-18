__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
from collections import Counter
from rdkit.Chem import Crippen
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem


s_bcs = set([
    'MaxEStateIndex', 'MinEStateIndex', 'FpDensityMorgan1',
    'EState_VSA1', 'HeavyAtomCount', 'NHOHCount', 'NOCount',
    'NumAliphaticCarbocycles', 'NumHeteroatoms', 'RingCount',
])


def bcs(mol):
    _descList = []
    dl = []
    for dp, function in Descriptors._descList:
        if dp in s_bcs:
            dl.append(function(mol))
            _descList.append((dp, function))
    return np.array(dl)


def crippen(mol):
    LogP = Crippen.MolLogP(mol)
    molar_refractivity = Crippen.MolMR(mol)
    dp = [LogP, molar_refractivity]
    return np.array(dp)


def fp(mols):
    fps = AllChem.GetMorganFingerprintAsBitVect(mols, radius=2, nBits=1024)
    return fps.ToBitString()


nt = ['A', 'C', 'G', 'U']


def dbl():
    pli = []
    for _, i in enumerate(nt):
        for _, j in enumerate(nt):
                pli.append(i + j)
    return pli


def tri():
    li = []
    for _, i in enumerate(nt):
        for _, j in enumerate(nt):
            for _, k in enumerate(nt):
                li.append(i + j + k)
    return li


def quad():
    li = []
    for _, i in enumerate(nt):
        for _, j in enumerate(nt):
            for _, k in enumerate(nt):
                for _, l in enumerate(nt):
                    li.append(i + j + k + l)
    return li


def ns(ins):
    ns_ = {}
    for _, i in enumerate(nt):
        ns_[i] = round(ins.count(i) / len(ins), 6)
    return ns_


def ds(ins):
    c = []
    for i in range(len(ins) - 1):
        c.append(ins[i] + ins[i + 1])
    freq_dict = dict(Counter(c))
    ds_ = {}
    keys = [*freq_dict.keys()]
    for _, i in enumerate(dbl()):
        if i in keys:
            ds_[i] = round(freq_dict[i] / (len(ins) - 1), 6)
        else:
            ds_[i] = 0
    return ds_


def ts(ins):
    c = []
    for i in range(len(ins) - 2):
        c.append(ins[i] + ins[i + 1] + ins[i + 2])
    freq_dict = dict(Counter(c))
    ts_ = {}
    keys = [*freq_dict.keys()]
    for _, i in enumerate(tri()):
        if i in keys:
            ts_[i] = round(freq_dict[i] / (len(ins) - 2), 6)
        else:
            ts_[i] = 0
    return ts_


def qs(ins):
    c = []
    for i in range(len(ins) - 3):
        c.append(ins[i] + ins[i + 1] + ins[i + 2] + ins[i + 3])
    freq_dict = dict(Counter(c))
    qs_ = {}
    keys = [*freq_dict.keys()]
    for _, i in enumerate(quad()):
        if i in keys:
            qs_[i] = round(freq_dict[i] / (len(ins) - 3), 6)
        else:
            qs_[i] = 0
    return qs_


def bseqs(ins, k):
    c = []
    for i in range(len(ins) - (k + 1)):
        c.append(ins[i] + ins[i + k + 1])
    freq_dict = dict(Counter(c))
    bseqs_ = {}
    keys = [*freq_dict.keys()]
    for _, i in enumerate(dbl()):
        if i in keys:
            bseqs_[i] = round(freq_dict[i] / (len(ins) - (k + 1)), 6)
        else:
            bseqs_[i] = 0
    return bseqs_


def aseqs(ins):
    cdict = {}
    for nt_ref in ['A', 'C', 'G', 'U']:
        cdict[nt_ref] = []
        cnt = 0
        for i, nt in enumerate(ins):
            if nt == nt_ref:
                cnt += 1
                cdict[nt_ref].append(cnt / (i + 1))
    cdict_ = {}
    for k, v in cdict.items():
        if v != []:
            cdict_[k] = sum(v) / len(v)
        else:
            cdict_[k] = 0
    return cdict_