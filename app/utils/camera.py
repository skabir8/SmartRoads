import cv2
import os
from utils.utils import draw_boxes
from utils.frontend import YOLO
import json
import time
from pprint import pprint
from utils.form import submit_form

class VideoCamera(object):
    def __init__(self):

        # Open a camera
        self.cap = cv2.VideoCapture(0)

        # Config paths
        self.config_path  = "./utils/config.json"
        self.weights_path = "./utils/weights.h5"

        with open(self.config_path) as config_buffer:
            self.config = json.load(config_buffer)

        self.yolo = YOLO(backend            = self.config['model']['backend'],
                        input_size          = self.config['model']['input_size'],
                        labels              = self.config['model']['labels'],
                        max_box_per_image   = self.config['model']['max_box_per_image'],
                        anchors             = self.config['model']['anchors'])
        self.yolo.load_weights(self.weights_path)

        # Initialize video recording environment
        self.last_recorded_time = time.time()

        # Thread for recording
        self.recordingThread = None

        # Reporting Variables
        self.report_interval = 5.0 # time to wait before sending another report in seconds
        self.conf_threshold = 0.4 # threshold for object to be considered a pothole (0.0-1.0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        self.curr_time = time.time()

        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)

            boxes = self.yolo.predict(frame)

            if (len(boxes) > 0):
                frame2 = draw_boxes(frame, boxes, self.config['model']['labels'])
                ret, jpeg = cv2.imencode('.jpg', frame2)

                if self.curr_time - self.last_recorded_time >= self.report_interval and boxes[0].get_score() >= self.conf_threshold:
                    print(boxes[0].get_score())
                    submit_form()
                    self.last_recorded_time = self.curr_time

                return jpeg.tobytes()

            return jpeg.tobytes()

        else:
            return None
