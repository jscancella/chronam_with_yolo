#pip install -r .\requirements.txt
#pip install pyqt5 lxml --upgrade

import torch

#setup data for training
#git clone https://github.com/tzutalin/labelImg
#cd labelImg 
#python.exe .\labelImg.py
#python.exe .\convertLabelImgToYoloFormat
#copy output txt and original jpeg files to train and test folder specified in dataset.yaml

#train model
#python train.py --img 640 --batch 16 --epochs 3 --data dataset.yaml --weights yolov5s.pt
#!cd yolov5 && python train.py --img 320 --batch 16 --epochs 2000 --data dataset.yml --weights yolov5s.pt --workers 2

#use to make sure it is setup correctly and is using GPU
#print("use GPU? ", torch.cuda.is_available())

#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
#img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
#results = model(img)

#results.show()  # or .print(), .save(), .crop(), .pandas(), etc.


#use our trained model
model = torch.hub.load('yolov5', 'custom', source='local', path='C:\\Users\\John\\Documents\\repos\\chronam yolov5\\runs\\train\\exp\\weights\\best.pt')
img = 'E:\\backups\\chronam\\test\\1842-04-23-01-0007.jpeg'  # or file, Path, PIL, OpenCV, numpy, list
results = model(img)
results.show()  # or .print(), .save(), .crop(), .pandas(), etc.