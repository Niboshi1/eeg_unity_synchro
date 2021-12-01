import numpy as np
import cv2
from datetime import datetime
import sys

def capture_camera(options):
    # Camera parameters
    trial_name1 = 'camera1_' + options['TRIAL_NAME']
    trial_name2 = 'camera2_' + options['TRIAL_NAME']
    fps = options['FPS']
    framesize = options['FRAMESIZE']
    max_rec = options['MAX_REC']
    limit = max_rec*3600*fps
    
    # Set caputure
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    # Start capture
    i = 0
    while(True):
        # Capture frame-by-frame
        # TODO: send TTL signal to EEG device 
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Calculate framerates
        sys.stdout.write("\r{}".format(cap1.get(5)))
        sys.stdout.flush()

        # write frame to video
        if i%limit == 0:
            video_name1 = trial_name1 + '_' + datetime.now().strftime("%Y-%m-%d_%H%M") + '.avi'
            video_name2 = trial_name2 + '_' + datetime.now().strftime("%Y-%m-%d_%H%M") + '.avi'

            out1 = cv2.VideoWriter(video_name1, fourcc, fps, framesize)
            out2 = cv2.VideoWriter(video_name2, fourcc, fps, framesize)
        i += 1
        out1.write(frame1)  
        out2.write(frame2)

        # display video
        im_h = cv2.hconcat([frame1, frame2])
        cv2.imshow('frame', im_h)

        # stop recording with Q
        if cv2.waitKey(1) & 0xFF == ord('q') or i == 2592000:
            break

    cap1.release()
    out1.release()
    cap2.release()
    out2.release()
    cv2.destroyAllWindows()