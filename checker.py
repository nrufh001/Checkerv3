
# import the modules

import cv2
import numpy as np
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
 
if __name__ == "__main__":
    # Set the format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
 
    # Set format for displaying path
    path = '.'
 
    # test
    # Initialize logging event handler
    event_handler = LoggingEventHandler()
 
    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
 
    # Start the observer
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
            img = cv2.imread('logging.src_path', 0)
            equ = cv2.equalizeHist(img)
            res = np.hstack((img, equ)) #stacking images side-by-side
            cv2.imwrite('res.png', res)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
