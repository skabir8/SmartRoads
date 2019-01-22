# Smart Road

## Demo

<p align="center"> <img src="demo.gif"/> </p>

## Running app

### Setting up vitural environment
```
virtualenv -p python3 venv
. venv/bin/activate
git clone git@github.com:skabir8/SmartRoads.git
cd SmartRoads/app/
pip3 install -r requirements.txt 
sudo apt-get install python3-tk
```

### Downloading weights
Download the weights from: https://drive.google.com/drive/folders/1npRY7FVNTBUodMt-qD67A1rlCXYoMFMp and place into app/utils

### Running app
```
python3 app.py
```

Once you open the flask app in your browser, there is a brief delay to set up the YOLO system and the camera.

## About
This application uses Tensorflow and Darknet to create weight files for a YOLO system that identifies potholes in real time via the camera. After recognizing a pothole and passing a identification threshold, it submits a pothole ticket to 311 to be fixed.

For this POC, it is build using flask and uses the computer's webcam to represent a phone or dashcam. 

The next steps of this project would be to port this over to an actual mobile application and possibly integrated into hardware. Our end goal is to put this on car dash cams so every possible pothole can be tracked and submitted to better aid the city.
