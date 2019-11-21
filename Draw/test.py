import cv2
import numpy as np
import pyautogui as p
import time
import keyboard
import os

'''
    Preprocess image and make contours (getting vertices of edges).
'''
image_location = 'C:/Users/csb003/Documents/NCHpython/Draw/Sea-Turtle.jpg'

x_length = 1200 # make x axis have this length. Different values will probably need different preprocessing arguments
im = cv2.imread(image_location, 0)
im = cv2.resize(im, None, None, x_length/im.shape[1], x_length/im.shape[1])

# adjusting values gives slightly different results. Changing x_length will probably require some arguments to be changed for better results
im = cv2.medianBlur(im, 7)
im = cv2.bilateralFilter(im, 4, 100, 100)
im = cv2.dilate(im, np.ones((5,5)))

th = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3) # higher last value = lower noise
contours, hier = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('contours', cv2.drawContours(np.zeros(im.shape)+255, contours, -1, (0,255,0), ))
cv2.imshow('preprocessed im', im)
cv2.imshow('thresholded im', th)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    Draw the image. Top left of image will be at the initial mouse position. Dont move your mouse. Press escape to exit.
'''
p.PAUSE = 0.011 # time between each mouse action. Lower values will get buggier
d = 1 # minimum distance between vertices to draw. lower value = longer time to draw but more accurate drawing
scale = 1 # size of image
d /= scale
time.sleep(3)
start = p.position()
prev_coor = (np.inf, np.inf) # previous coordinate to calculate distance from
brk = False # true means it exits the loop
for cont in contours:
    p.moveTo(int(cont[0][0,0] * scale + start.x), int(cont[0][0,1] * scale + start.y)) # move to start of contour
    p.mouseDown()
    for coor in cont[1:]: 
        if ((coor[0,0] - prev_coor[0])**2 + (coor[0,1] - prev_coor[1])**2)**0.5 >= d: # check Euclidean distance from previous coordinate
            prev_coor = coor[0]
            p.moveTo(int(coor[0,0] * scale + start.x), int(coor[0,1] *  scale + start.y)) # move cursor
        if keyboard.is_pressed('esc'): # exit when escape is pressed
            brk = True
            break
    p.mouseUp()
    if brk:
        break

'''
    Sequence of coordinates (y-down, x-right) to draw each letter
'''
letters = {
    'A':((4,0),(0,0),(0,4),(2,4),(2,0),(2,4),(4,4)),
    'B':((0,0),(0,4),(2,4),(2,1),(2,4),(4,4),(4,0),(0,0)),
    'C':((0,4),(0,0),(4,0),(4,4)),
    'D':((0,0),(0,3),(1,4),(4,4),(4,0),(0,0)),
    'E':((2,0),(2,4),(0,4),(0,0),(4,0),(4,4)),
    'F':((0,4),(0,0),(2,0),(2,4),(2,0),(4,0)),
    'G':((0,4),(0,0),(4,0),(4,4),(2,4),(2,2)),
    'H':((0,0),(4,0),(2,0),(2,4),(0,4),(4,4)),
    'I':((0,0),(0,4),(0,2),(4,2),(4,0),(4,4)),
    'J':((0,0),(0,4),(0,2),(4,2),(4,0),(2,0)),
    'K':((0,0),(4,0),(2,0),(0,4),(2,0),(4,4)),
    'L':((0,0),(4,0),(4,4)),
    'M':((4,0),(0,0),(2,2),(0,4),(4,4)),
    'N':((4,0),(0,0),(4,4),(0,4)),
    'O':((0,0),(4,0),(4,4),(0,4),(0,0)),
    'P':((4,0),(0,0),(0,4),(2,4),(2,0)),
    'Q':((4,4),(4,0),(0,0),(0,4),(4,4),(2,2)),
    'R':((4,0),(0,0),(0,4),(2,4),(2,0),(2,2),(4,4)),
    'S':((4,0),(4,4),(2,4),(2,0),(0,0),(0,4)),
    'T':((0,0),(0,4),(0,2),(4,2)),
    'U':((0,0),(4,0),(4,4),(0,4)),
    'V':((0,0),(4,2),(0,4)),
    'W':((0,0),(4,0),(2,2),(4,4),(0,4)),
    'X':((0,0),(4,4),(2,2),(4,0),(0,4)),
    'Y':((0,0),(2,2),(0,4),(4,0)),
    'Z':((0,0),(0,4),(4,0),(4,4)),
}

'''
    Draw text
'''
p.PAUSE = 0.03 # time between each mouse action
text = 'the quick\nbrown fox jumps\nover the\nlazy dog'.upper()
size = 5 # size of letter / 4 in pixels

time.sleep(3)
orig_pos = p.position()
pos = [orig_pos.x, orig_pos.y] # allows it to be mutable
brk = False
for char in text:
    if char is '\n': # move cursor to 1 char length under original position for a new line
        pos[1] += int(5 * size)
        pos[0] = orig_pos[0]
        continue
        
    if char is ' ': # move cursor right by 1 char
        pos[0] += int(5*size)
        continue
        
    coors = letters[char]
    p.moveTo(pos[0] + coors[0][1] * size, pos[1] + coors[0][0] * size) # move to start of letter
    p.mouseDown()
    for coor in coors[1:]:
        p.moveTo(pos[0] + coor[1] * size, pos[1] + coor[0] * size) # move cursor
        if keyboard.is_pressed('esc'): # exit when escape is pressed
            brk = True
            break
    if brk:
        break
    p.mouseUp()
    pos[0] += int(5 * size) # change position for next character