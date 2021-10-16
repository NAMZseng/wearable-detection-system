import numpy as np
from trainer import Trainer
from modules.CNN_LSTM_ATTN import CNN_RNN_Attention_Model
import config

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 提前加载神经网络的内存模型，从而减少post请求的响应耗时
model = CNN_RNN_Attention_Model(config.input_size, config.hid_size, config.rnn_type, config.bidirectional)
bp = Trainer(model, config.lr, config.batch_size, config.num_epochs, config.patience)
# 设置为绝对路径，防止django运行时路径context不一致导致文件找不到的问题
model = bp.load(
    "/home/nanrong/wearable_detection_backend/deep_learning/BP_project/model/01_best_model_fold5_epoc118.pth")


@api_view(['POST'])
def get_bp_predict(request):
    """
    对安卓的传入的5s内ecg,ppg的信号数据进行神经网络模型预测
    :param request: post请求的json数据
    :return: 5s内的平均收缩压SBP,舒张压DBP
    """
    if request.method == 'POST':
        ecg = request.data.get('ecg')  # list
        ppg = request.data.get('ppg')

        # list to array in shape (1, 625)
        ecg = np.array(ecg).reshape(1, 625)
        ppg = np.array(ppg).reshape(1, 625)

        # (1, 625) to (2, 625)
        net_input_data = np.append(ecg, ppg, axis=0)

        predict_result = bp.predict(net_input_data, model)

        return Response(predict_result, status=status.HTTP_200_OK)
