import cv2

# 0 means we want to use the default camera
# put the path of some video file to play
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read() # returning two objects

    print(ret)
    cv2.imshow('video', frame)

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