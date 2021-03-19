import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
    # images, videos and live video
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)



img = cv.imread("./photos/cat.jpg")
cv.imshow("Cat", img)

resized_image = rescaleFrame(img)
cv.imshow("Cat resized", resized_image)


capture = cv.VideoCapture("./video/dog.mp4")




while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow("video", frame)
    cv.imshow("video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break




capture.release()
cv.destroyAllWindows()






cv.waitKey(0)