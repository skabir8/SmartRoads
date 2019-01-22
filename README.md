# Smart Road

## How it Looks Like

[![](https://puu.sh/CAsha/8e14886b6e.jpg)](https://drive.google.com/file/d/1AsgKN1kLrnYira_I0v6MDGABSI2Bhhk0/view)

[Watch the demo](https://drive.google.com/file/d/1AsgKN1kLrnYira_I0v6MDGABSI2Bhhk0/view)

## Installing Requirements
Install the necessary pre-requisites by

```
pip3 install -r requirements.txt
```

Download the weights from: https://drive.google.com/drive/folders/1npRY7FVNTBUodMt-qD67A1rlCXYoMFMp and place into app/utils

## Running app

```
python3 app.py
```

Once you open the flask app in your browser, it should take some time to set up the YOLO system and the camera.

## About
This application uses Tensorflow and Darknet to create weight files for a YOLO system that identifies potholes in real time via the camera. After recognizing a pothole and passing a identification threshold, it submits a pothole ticket to 311 to be fixed.

For this POC, it is build using flask and uses the computer's webcam to represent a phone or dashcam. The next steps of this project would be to port this over to an actual mobile application and possibly integrated into hardware.