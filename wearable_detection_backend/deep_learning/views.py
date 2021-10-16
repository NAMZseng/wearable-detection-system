import numpy as np

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main import bp_predict


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

        predict_result = bp_predict(net_input_data)

        return Response(predict_result, status=status.HTTP_200_OK)
