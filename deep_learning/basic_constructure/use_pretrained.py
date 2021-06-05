import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import alexnet
#vision의 사용가능한 모델
'''
from .alexnet import *
from .resnet import *
from .vgg import *
from .squeezenet import *
from .inception import *
from .densenet import *
from .googlenet import *
from .mobilenet import *
from .mnasnet import *
from .shufflenetv2 import *
from . import segmentation
from . import detection
from . import video
from . import quantization
'''
# model = alexnet() #그냥모델
# model
# model = alexnet(pretrained=True) #가중치까지 가져온 모델
# model

#vgg가져와서 feature extract 하기 위해 분류기 빼고 학습 멈춰 !
from torchvision.models import vgg19_bn 
model = vgg19_bn(pretrained=True)
num_classes = 18
model = vgg19_bn(pretrained=True)
model.classifier = nn.Sequential(
    nn.Linear(512 * 7 * 7, 4096),
    nn.ReLU(True),
    nn.Dropout(),
    nn.Linear(4096, 4096),
    nn.ReLU(True),
    nn.Dropout(),
    nn.Linear(4096, num_classes),
)

# Freeze only feauture parts
model.features.requires_grad_(False)
for param, weight in model.named_parameters():
    print(f"param {param:20} required gradient? -> {weight.requires_grad}")

import torch.nn.init as init
#갈아끼운 분류기 부분만 가중치 초기화
def initialize_weights(model):
    """
    Initialize all weights using xavier uniform. 
    For more weight initialization methods, check https://pytorch.org/docs/stable/nn.init.html
    """
    for m in model.modules():
        if isinstance(m, nn.Conv2d):
            init.xavier_uniform_(m.weight.data)
            if m.bias is not None:
                m.bias.data.zero_()
        elif isinstance(m, nn.BatchNorm2d):
            m.weight.data.fill_(1)
            m.bias.data.zero_()
        elif isinstance(m, nn.Linear):
            m.weight.data.normal_(0, 0.01)
            m.bias.data.zero_()

model = vgg19_bn(pretrained=True)

# Initialize only classifier part
initialize_weights(model.classifier)

#timm으로 추가적인 pretraind 모델 이용
!pip install timm
import timm

m = timm.create_model('mobilenetv3_large_100', pretrained=True)
m.eval()