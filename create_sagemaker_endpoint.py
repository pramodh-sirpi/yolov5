# -*- coding: utf-8 -*-
"""yolov5-sagemaker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nTcocTlAvfREXl8DGcjIGobLtJpew_zH
"""
!pip install sagemaker
!pip install tensorflow
import os
import tensorflow as tf
from tensorflow.keras import backend
from sagemaker.tensorflow import TensorFlowModel

ls

#!cd yolov5

#!git clone https://github.com/ultralytics/yolov5
#!cd yolov5
!pip install -r requirements.txt
#!python export.py --weights yolov5l.pt --include saved_model --nms
#!mkdir export && mkdir export/Servo
#!mv yolov5l_saved_model export/Servo/1
#!tar -czvf model.tar.gz export
#!aws s3 cp model.tar.gz "s3://drivex-label/model.tar.gz"

model_data = 's3://testreprex1l/model.tar.gz'
role = 'arn:aws:iam::920644990528:role/mlops'

model = TensorFlowModel(model_data=model_data, 
                        framework_version='2.8', role=role)

INSTANCE_TYPE = 'ml.m5.xlarge'
ENDPOINT_NAME = 'yolov5-reprex1'

predictor = model.deploy(initial_instance_count=1, 
                         instance_type=INSTANCE_TYPE,
                         endpoint_name=ENDPOINT_NAME)

