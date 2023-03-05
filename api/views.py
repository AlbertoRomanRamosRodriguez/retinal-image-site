# Create your views here.
from torchvision import models, transforms
from PIL import Image

from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import OFSerializer
from .forms import ImageUploadForm
from .models import OFundus

import requests

import torch.nn as nn
import base64
import torch
import os
import io

class_mappings = {
    0:'No DR', 
    1:'DR-1', 
    2:'DR-2', 
    3:'DR-3', 
    4:'DR-4'
}

FILENAME = 'MobileNetV3_Grading_23_Feb_23_17_04'
PATH = os.path.sep.join(['models_pt', f'{FILENAME}.pt'])

model_ft  = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.IMAGENET1K_V1)
num_ftrs = model_ft.classifier[-1].in_features
model_ft.classifier[-1] = nn.Linear(num_ftrs, len(class_mappings.keys()))
model_ft.load_state_dict(torch.load(PATH))
model_ft.eval()

def preprocess_image(img_bytes):
    """
    Preprocesses an image stream by resizing, center-cropping, converting to Tensor
    and normalizing.

    It adds an extra dimension as required by the model.
    """
    img_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(img_bytes)
    return img_transforms(image).unsqueeze(0)

def get_prediction(img_bytes):
    img_tensor = preprocess_image(img_bytes)
    outputs = model_ft.forward(img_tensor)
    _, y_hat = outputs.max(1)
    label = class_mappings[y_hat.item()]
    print(label)
    return label


class OFViewSet(viewsets.ModelViewSet):
    queryset = OFundus.objects.all().order_by('id')
    serializer_class =  OFSerializer

    response_body = {'status':'Something went wrong'}

    def create(self, request, *args,  **kwargs):
        fundus_data = request.data
        image = fundus_data['image'].file
                
        try:
            predicted_label = get_prediction(image)
        except RuntimeError as re:
            print(re)
        else:
            new_ofundus = OFundus.objects.create(
                image = fundus_data['image'],
                class_name = predicted_label,
            )
            new_ofundus.save()

            response_body = OFSerializer(new_ofundus).data

        return Response(data = response_body)