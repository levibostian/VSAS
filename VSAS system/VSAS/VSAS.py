from vsasGUI.VSASmainScreen import *
from Motion.MotionDetector import *

def main():
    motion = MotionDetector()
    motionThread = threading.Thread(None, motion)
    motionThread.daemon = True #daemon threads are background task threads
    motionThread.start()

    vsas = Application(motion, root)
    vsasThread = threading.Thread(None, vsas)
    vsasThread.start()

    
    
main() 
