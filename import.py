
# For automated test log result directly in the csv
# load the pretinrained network from Keras Applications
#from keras import backend as K
#from keras.backend.tensorflow_backend import set_session
#from tensorflow.keras.applications.efficientNetB7 import efficientNetB7
#import keras
ImageFile.LOAD_TRUNCATED_IMAGES = True
from IPython.display import Image, HTML, display
from PIL import Image, ImageEnhance
from PIL import ImageFile
from cycler import cycler
from functions import val_train_bases,str_to_class,new_format_classification,get_classes
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
from multiprocessing import Pool, cpu_count
from operator import itemgetter
from os import path
from rmac import RMAC
from scipy import spatial
from shutil import copyfile
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.densenet import DenseNet121, preprocess_input, decode_predictions# input shape= 224x224 
from tensorflow.keras.applications.densenet import DenseNet169, preprocess_input
from tensorflow.keras.applications.densenet import DenseNet201, preprocess_input
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input,decode_predictions# input shape= 299x299
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input,decode_predictions# input shape= 299x299
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.nasnet import NASNetLarge, preprocess_input
from tensorflow.keras.applications.nasnet import NASNetMobile, preprocess_input
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions #224*224
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.applications.xception import Xception, preprocess_input, decode_predictions #299*299
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Lambda
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Activation, Flatten,Lambda
from tensorflow.keras.layers import Dense, Lambda
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Sequential,Model, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
import argparse
import csv
import cv2
import datetime
import imghdr
import math
import matplotlib
import ntpath
import numpy as np
import operator
import os
import os.path
import pickle
import pickle as pkl
import shutil
import shutil 
import sys
import tensorflow as tf
import time
import urllib.request
import warnings
import zipfile
