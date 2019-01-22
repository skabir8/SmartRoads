import cv2
import os
from utils.utils import draw_boxes
from utils.frontend import YOLO
import json
import time
from pprint import pprint

class VideoCamera(object):
    def __init__(self):

        # Open a camera

        self.cap = cv2.VideoCapture(0)
        self.config_path  = "./utils/config.json"
        self.weights_path = "./utils/weights.h5"

        with open(self.config_path) as config_buffer:
            self.config = json.load(config_buffer)

        yolo = YOLO(backend             = self.config['model']['backend'],
                    input_size          = self.config['model']['input_size'],
                    labels              = self.config['model']['labels'],
                    max_box_per_image   = self.config['model']['max_box_per_image'],
                    anchors             = self.config['model']['anchors'])
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
