import cv2
import numpy as np
 
# define a function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONUP:
      print(f'({x},{y})')

#    elif event == cv2.EVENT_RBUTTONDOWN:
      b,g,r = (frame[x,y])
      print(r,g,b)
      
      # put coordinates as text on the image
      cv2.putText(frame, f'({x},{y})',(x,y),
      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)


vid = cv2.VideoCapture(0)

# create a window
cv2.namedWindow('Point Coordinates')

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# display video
while True:
   ret, frame = vid.read()
#    cv2.imshow('frame',frame)
   cv2.imshow('Point Coordinates', frame)
   if cv2.waitKey(1000) & 0xFF == ord('f'):
        break
cv2.destroyAllWindows()