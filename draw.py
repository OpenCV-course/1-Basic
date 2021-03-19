import cv2 as cv
import numpy as np


#blank
blank = np.zeros((500,500,3), dtype = "uint8")
cv. imshow("Blank",blank)


# 1. Paint the image a certain colour
#all blank

blank[:] = 0,255,0 #green
cv.imshow("Green",blank)
'''
#piece the blank
blank[200:300, 300:400] = 0,0,255 #red
cv.imshow("Red",blank)


# 2. Draw a Rectangle, cv.rectangle(objet, origin,size, line thickness)
cv.rectangle(blank,(0,0), (250,250),(0,255,0), thickness = 3 )
cv.imshow("Rectangle",blank )


#Rectagle filled
cv.rectangle(blank,(0,0), (250,250),(0,255,0), thickness = cv.FILLED ) # same thickness = -1
cv.imshow("Rectangle Filled",blank )

#half blank
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness = -1 )
cv.imshow("Half Filled",blank )



# 3. Draw a circle, cv.circle(objet, origin,size, line thickness)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40, (0,0,250),thickness = -1)
cv.imshow("circle",blank)

#4. Draw line
cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),thickness = 3)
cv.imshow("line",blank)
cv.line(blank, (100,250),(300,400), (255,255,255),thickness = 3)
cv.imshow("line 2",blank)

#5. Write text
cv.putText(blank,"Hello",(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow("text", blank)
'''


cv.waitKey(0)

