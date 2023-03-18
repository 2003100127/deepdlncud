__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../../')
from Bio import SeqIO


def fasta(fasta_fpn):
    sequence = []
    for seq in SeqIO.parse(fasta_fpn, "fasta"):
        # print(seq.seq)
        sequence.append(str(seq.seq))
    sequence = ''.join(sequence)
    if sequence == '':
        print('The sequence is empty.')
    return sequence