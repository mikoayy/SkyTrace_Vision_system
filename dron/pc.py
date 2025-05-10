import cv2
from model import Camera

cam = Camera(cam_idx="http://192.168.1.65:5000")
cam.run()

    
    