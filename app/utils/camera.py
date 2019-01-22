import cv2
import os
from utils.utils import draw_boxes
from utils.frontend import YOLO
import json
import time
from pprint import pprint

class VideoCamera(object):
    def __init__(self):
        config_path  = "./config.json"
        weights_path = "./weights.h5"
        # Open a camera
        self.cap = cv2.VideoCapture(0)
        yolo = YOLO(backend             = "Full Yolo",
                    input_size          = 416,
                    labels              = [0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828],
                    max_box_per_image   = 10,
                    anchors             = ["pothole"])
        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recordingThread = None

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)

            # Record video


            return jpeg.tobytes()

        else:
            return None
