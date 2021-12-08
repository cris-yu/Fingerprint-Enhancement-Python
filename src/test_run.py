import fingerprint_enhancer								# Load the library
import cv2

img = cv2.imread('image_path', 0)						# read input image
out = fingerprint_enhancer.enhance_Fingerprint(img)		# enhance the fingerprint image
cv2.imshow('enhanced_image', out);						# display the result
cv2.waitKey(0)											# hold the display window
