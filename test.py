import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture('/home/burhan/WEST/1.mp4')

while True:

    ret, frame = cap.read()
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #out = cv2.VideoWriter('cap_output.mp4',fourcc, 30.0, (500,400))

    if ret == True:
	res = cv2.resize(frame, (500,400))
     	#out.write(res)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',res)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
