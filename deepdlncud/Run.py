__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from deepdlncud.Pipe import fetch


def drestruct(data, met):
    if met == 'ConvMixer64' or met == 'DenseNet':
        return np.reshape(data, [-1, 37, 37, 1])
    else:
        return data


class predict(object):

    def __init__(
            self,
            smile_fpn,
            fasta_fpn,
            method,
            model_fp,
            sv_fpn,
    ):
        self.method = method
        self.model_fp = model_fp
        self.sv_fpn = sv_fpn
        self.ind = fetch(
            smile_fpn=smile_fpn,
            fasta_fpn=fasta_fpn,
        )

    def m(self, ):
        loaded_model = tf.keras.models.load_model(self.model_fp)
        pret = loaded_model.predict(drestruct(self.ind, self.method), batch_size=1)
        t = []
        if pret[0][1] > pret[0][0]:
            t.append([pret[0][1], 'Upregulation'])
        else:
            t.append([pret[0][0], 'Downregulation'])
        df = pd.DataFrame(t, columns=['prob', 'predicted_type'])
        df.to_csv(
            self.sv_fpn,
            sep='\t',
            header=True,
            index=False,
        )
        return df


if __name__ == "__main__":
    p = predict(

        # smile_fpn='data/example/6918837.txt',
        # fasta_fpn='data/example/lnc-CPO-4.fasta',

        smile_fpn='data/example/60606.txt',
        fasta_fpn='data/example/HIF1A-AS1.fasta',

        method='DenseNet',
        # method='CNN',
        # method='ConvMixer64',
        # method='DSConv',
        # method='LSTMCNN',
        # method='MobileNet',
        # method='ResNet18',
        # method='ResNet50',
        # method='SEResNet',

        model_fp='model/densenet',
        # model_fp='model/cnn',
        # model_fp='model/convmixer64',
        # model_fp='model/dsconv',
        # model_fp='model/lstmcnn',
        # model_fp='model/mobilenetv2',
        # model_fp='model/resnet_prea18',
        # model_fp='model/resnet_prea50',
        # model_fp='model/scaresnet',

        sv_fpn='./pred.deepdlncud',
    )
    print(p.m())

