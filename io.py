import cv
import cv2

def outputImage(imgPath, img):
	cv2.imwrite(imgPath, img)

def readImageGrayscale8Bit(imgPath):
	print imgPath
	img = cv2.imread(imgPath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	return img

def showImage(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()