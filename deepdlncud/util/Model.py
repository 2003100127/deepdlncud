__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


def drestruct(data, met):
    if met == 'ConvMixer64' or met == 'DenseNet':
        return np.reshape(data, [-1, 37, 37, 1])
    else:
        return data


class Model:

    def __init__(
            self,
            mat_np,
            method,
            model_fp,
            sv_fpn,
            batch_size=100,
            thres=0.5,
    ):
        self.method = method
        self.model_fp = model_fp
        self.mat_np = mat_np
        self.sv_fpn = sv_fpn
        self.batch_size = batch_size
        self.thres = thres

    def m(self, ):
        loaded_model = tf.keras.models.load_model(self.model_fp)
        pred = loaded_model.predict(drestruct(self.mat_np, self.method), batch_size=self.batch_size)
        df = pd.DataFrame(pred[:, [1]], columns=['prob_up'])
        df['pred_type'] = df['prob_up'].apply(lambda x: 'Upregulation' if x > self.thres else 'Downregulation')
        print(df)
        if self.sv_fpn:
            df.to_csv(
                self.sv_fpn,
                sep='\t',
                header=True,
                index=False,
            )
        return df


if __name__ == "__main__":
    p = Model(
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

        mat_np=None,

        sv_fpn='./pred.deepdlncud',
    )
    print(p.m())

