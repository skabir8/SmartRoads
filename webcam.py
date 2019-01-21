#! /usr/bin/env python

import argparse
import os
import cv2
import numpy as np
from tqdm import tqdm
from preprocessing import parse_annotation
from utils import draw_boxes
from frontend import YOLO
import json
from pprint import pprint
import time

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"
cap = cv2.VideoCapture(0)

argparser = argparse.ArgumentParser(
    description='Train and validate YOLO_v2 model on any dataset')

argparser.add_argument(
    '-c',
    '--conf',
    help='path to configuration file')

argparser.add_argument(
    '-w',
    '--weights',
    help='path to pretrained weights')

argparser.add_argument(
    '-i',
    '--input',
    help='path to an image or an video (mp4 format)')

#cap = cv2.VideoCapture(0)

def _main_(args):
    config_path  = "/home/shariar/Desktop/potholes-detection/config.json"
    weights_path = "/home/shariar/Desktop/potholes-detection/trained_wts.h5"


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
    last_recorded_time = time.time()
    while True:
        # Capture frame-by-frame
        curr_time = time.time()
        ret, frame = cap.read()
        if curr_time - last_recorded_time >= 2.0:
            cv2.imshow('', frame)
            boxes = yolo.predict(frame)
            if (len(boxes) > 0):
                b = boxes[0]
                s = b.get_score()
                data = [b.c, b.score, s]
                pprint(data)
            frame2 = draw_boxes(frame, boxes, config['model']['labels'])
            # Display the resulting frame
            cv2.imshow('', frame2)
            last_recorded_time = curr_time
        else:
            cv2.imshow('', frame)
            boxes = yolo.predict(frame)
            frame2 = draw_boxes(frame, boxes, config['model']['labels'])
            cv2.imshow('', frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# When everything done, release the capture
if __name__ == '__main__':
    args = argparser.parse_args()
    _main_(args)
    cap = cv2.VideoCapture(0)
