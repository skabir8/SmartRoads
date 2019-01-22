#! /usr/bin/env python

import os
import cv2
from utils import draw_boxes
from frontend import YOLO
import json
import time
from pprint import pprint

cap = cv2.VideoCapture(0)

def _main_():
    config_path  = "./config.json"
    weights_path = "./weights.h5"

    with open(config_path) as config_buffer:
        config = json.load(config_buffer)

    ###############################
    #   Make the model
    ###############################

    ###############################
    #   Load trained weights
    ###############################

    yolo.load_weights(weights_path)

    ###############################
    #   Predict bounding boxes
    ###############################

    last_recorded_time = time.time()

    while True:
        curr_time = time.time()

        # Capture frame-by-frame
        ret, frame = cap.read()

        # checks if 2 or more seconds have passed since last [placeholder]
        if curr_time - last_recorded_time >= 2.0:
            cv2.imshow('', frame)
            boxes = yolo.predict(frame)

            # [placeholder for api call]
            if (len(boxes) > 0):
                print(boxes[0].get_score())

            frame2 = draw_boxes(frame, boxes, config['model']['labels'])

            # Display the resulting frame
            cv2.imshow('', frame2)

            # Stores last time frame was drawn
            last_recorded_time = curr_time
        else:
            cv2.imshow('', frame)
            boxes = yolo.predict(frame)
            frame2 = draw_boxes(frame, boxes, config['model']['labels'])
            cv2.imshow('', frame2)

        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# When everything done, release the capture
if __name__ == '__main__':
    _main_()
