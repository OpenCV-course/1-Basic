import cv2 as cv

img = cv.imread("./photos/park.jpg")
cv.imshow("Park", img)


#Converting a grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

#blur (5,5) nivel blur
blur = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)


#Edge cascade
canny = cv.Canny(img, 125,175)
#cv.imshow("Canny edge", canny)

#best cany
canny = cv.Canny(blur, 125,175)
#cv.imshow("Canny edge", canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
#cv.imshow("Dilated", canny)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations = 3)
#cv.imshow("Eroded", eroded)

#Resize 

resize = cv.resize(img, (1000,1000))
#cv.imshow("Resize", resize)

# Cropping
crope = img[50:200, 200:400]
cv.imshow("Crope",crope)
 
cv.waitKey(0)