#!/usr/bin/env python

from __future__ import print_function
import math
import time
import numpy as np
import cv2


AREA_SIZE = 800 #in pixels?
#expected frame sizes
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FRAME_WIDTH_HALF = int(FRAME_WIDTH/2)
FRAME_HEIGHT_HALF = int(FRAME_HEIGHT/2)
CENT_BOX_SIZE = 50

cap = cv2.VideoCapture(0)

def main():

	while True:
		ret, frame = cap.read()
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		lower_yellow = np.array([20,110,110])
		upper_yellow = np.array([40,255,255])

		yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

		(contours,_) = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		#draw central bounding box
		frame = cv2.rectangle(frame, (FRAME_WIDTH_HALF-CENT_BOX_SIZE,FRAME_HEIGHT_HALF-CENT_BOX_SIZE), 
			(FRAME_WIDTH_HALF+CENT_BOX_SIZE,FRAME_HEIGHT_HALF+CENT_BOX_SIZE), (255,0,255), 5)
		centr_bound_x = [FRAME_WIDTH_HALF-CENT_BOX_SIZE,FRAME_WIDTH_HALF+CENT_BOX_SIZE]
		centr_bound_y = [FRAME_HEIGHT_HALF-CENT_BOX_SIZE,FRAME_HEIGHT_HALF+CENT_BOX_SIZE]
		for contour in contours:
			area = cv2.contourArea(contour)

			if(area>AREA_SIZE):
				x,y,w,h = cv2.boundingRect(contour)
				centre = (x+(w/2), y+(h/2)) #determining centre of boundingRect
				frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 5)
				# print("Centre - x: {}, y: {}".format(centre[0],centre[1]))
				# print("Boundaries - x:{},{}  y:{},{}".format(centr_bound_x[0],centr_bound_x[1],centr_bound_y[0],centr_bound_y[1]))

				if (centre[0] in range(centr_bound_x[0],centr_bound_x[1])) & (centre[1] in range(centr_bound_y[0], centr_bound_y[1])):
					print("Within bounding box!\n")

				distance_from_centre = [(centre[0]-FRAME_WIDTH_HALF),-(centre[1]-FRAME_HEIGHT_HALF)]

				print("Distance to move:({},{})\n".format(distance_from_centre[0],distance_from_centre[1]))
				# else:
				# 	print("Outside bounding box\n")

		cv2.imshow("Colour Tracking", frame)

		if cv2.waitKey(30) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__=="__main__":
	main()