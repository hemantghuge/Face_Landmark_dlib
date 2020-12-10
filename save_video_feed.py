
# Python program to save a
# video using OpenCV
import cv2
import time


# Create an object to read
# from camera
VIDEO_INPUT = 'rtsp://admin:admin123@192.0.9.152'
VIDEO_INPUT = 0
cap = cv2.VideoCapture(VIDEO_INPUT)

# We need to check if camera
# is opened previously or not
if (cap.isOpened() == False):
    print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)
#fps = cap.get(5)
# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter('face.avi', fourcc, 25, size)
init_time = time.time()
counter = 0

while cap.isOpened():
	counter += 1
	grabbed, frame = cap.read()
	if not grabbed:
		cap.release()
		cap = cv2.VideoCapture(VIDEO_INPUT)
		continue

	if counter < 10000:
		print(counter)
		img = frame
		result.write(img)

		# Display the frame
		# cv2.imshow('Frame', img)

		key = cv2.waitKey(1)
		if key == ord('q'):
			cv2.destroyAllWindows()
			break
		if int(time.time()-init_time) == 1200:
			cv2.destroyAllWindows()
			break
	else:
		break

# When everything done, release
# the video capture and video
# write objects
cap.release()
result.release()

# Closes all the frame
print("The video was successfully saved")
