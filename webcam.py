#! /usr/bin/env python

import os
import cv2
import numpy as np
from tqdm import tqdm
from preprocessing import parse_annotation
from utils import draw_boxes
from frontend import YOLO
import json
from pprint import pprint


os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"
cap = cv2.VideoCapture(0)

def _main_():
    config_path  = "./config.json"
    weights_path = "./trained_wts.h5"


    with open(config_path) as config_buffer:
        config = json.load(config_buffer)

    ###############################
    #   Make the model
    ###############################
    yolo = YOLO(backend             = "Full Yolo",
                input_size          = config['model']['input_size'],
                labels              = config['model']['labels'],
                max_box_per_image   = config['model']['max_box_per_image'],
                anchors             = config['model']['anchors'])

    ###############################
    #   Load trained weights
    ###############################

    yolo.load_weights(weights_path)

    ###############################
    #   Predict bounding boxes
    ###############################

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        boxes = yolo.predict(frame)

        if (len(boxes) > 0):
            print(boxes[0].get_score())

        frame2 = draw_boxes(frame, boxes, config['model']['labels'])

        # Display the resulting frame
        cv2.imshow('', frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# When everything done, release the capture
if __name__ == '__main__':
    _main_()
