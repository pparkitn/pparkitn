import numpy as np
import cv2
from PIL import *
from PIL import Image
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import boto3
from botocore.exceptions import NoCredentialsError
from torchvision import datasets, transforms, models
from torch.autograd import Variable
import os.path
from os import path
import paho.mqtt.client as mqtt 

mqtt_addr = '192.168.2.52'
mqtt_port = 1883
LOCAL_MQTT_TOPIC="camera/found_face"

client = mqtt.Client()                                      
client.connect(mqtt_addr,mqtt_port,120)   

# ====================================================================================

#S3 Keys
ACCESS_KEY = 'X'
SECRET_KEY = 'X'

GPU=0
ARCH = 'resnet50'
classes = ["angry", "disgusted", "fearful", "happy", "neutral", "sad", "suprise"]

# ====================================================================================

def download_from_aws(s3_file, bucket):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    
    try:
        s3.download_file(bucket, s3_file, s3_file)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

# ====================================================================================

torch.cuda.set_device(GPU)

NUM_CLASSES = 7
model = models.__dict__[ARCH](pretrained = True)
inf = model.fc.in_features
model.fc = nn.Linear(inf, NUM_CLASSES)
model.cuda(GPU)

# ====================================================================================

saved_model_name = "M1_43_acc1_tensor(62.4547, device='cuda:0')_resnet50.tar"
if os.path.exists(saved_model_name):
    print("Got the Model")
else:
    print("Downloading Model")
    download_from_aws(saved_model_name, 'w251-homework3')

loc = 'cuda:{}'.format(GPU)
checkpoint = torch.load(saved_model_name, map_location=loc)
model.load_state_dict(checkpoint['state_dict'])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

test_transforms = transforms.Compose( [ 
                                        transforms.Grayscale(num_output_channels=3),
                                        transforms.ToTensor(),

                                     ])
# ====================================================================================

def predict_image(image):
    
    model.eval()
    with torch.no_grad():
        image_tensor = test_transforms(image).float()
        image_tensor = image_tensor.unsqueeze_(0)
        input = Variable(image_tensor)
        input = input.to(device)
        output = model(input)
        index = output.data.cpu().numpy().argmax()
       
    return index

# ====================================================================================
to_pil = transforms.ToPILImage()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   
    cv2.imshow('frame',gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        
        if np.sum([roi_gray]) != 0:

            image = to_pil(roi_gray)
            index = predict_image(image)

            label_position = (x-60, y)
            label = "I am " + classes[index]
            cv2.putText(gray,label,label_position,cv2.FONT_HERSHEY_COMPLEX,2,(255, 0, 0),3,cv2.LINE_AA)

            cv2.imshow('frame',roi_gray)
            cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('frame',gray)

            msg = str(classes[index]) 
            print(msg)
            ret_val = client.publish(LOCAL_MQTT_TOPIC,msg,qos=0, retain=False)
            print(ret_val)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()