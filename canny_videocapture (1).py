import cv2
import numpy as np

# 0 means we want to use the default camera
# put the path of some video file to play
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read() # returning two objects

    print(ret)

    # thresholding the image
    # Converting the color channel of our image from bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Change them as per your requirements
    lower_color = np.array([30, 150, 50])
    higher_color = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_color, higher_color)

    # Bitwise and with frame
    # mask is a binary image with 2 colors, some pixles = [0, 0 , 0], others will have [255, 255, 255]

    # Masked image
    # compute src1 AND src2 if mask != 0
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # change these threshold values
    edges = cv2.Canny(result, 100, 200)

    # cv2.imshow('video', frame)
    cv2.imshow('edges', edges)

    # 0xFF = 1111 1111 (in binary) (8 bit number)
    # cv2.waitkey('interval in ms') return 32 bit binary number
    # cv2.waitKey(1) & 0xFF = extract the last 8 bits of the binary notation of that key which was pressed
    # ord('q') = 8 bit binary number corresponding to letter 'q'

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# safety check to release the memory
# optional 
vid.release()
cv2.destroyAllWindows()