import cv2 as cv
import numpy as np

# sort function sort points Top-left, Top-right, Bottom-right, Bottom-left
def sortPoint(pts):
    rect = np.zeros((4,2), dtype = "float32")
    
    s = np.sum(pts, axis = 1) # Sum along row
    rect[0] = pts[np.argmin(s)] # Top-left
    rect[2] = pts[np.argmax(s)] # Bottom-right
    print(np.argmin(s),np.argmax(s))
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)] # Top-right
    rect [3] = pts[np.argmax(diff)] # Bottom-left
    
    return rect

def perspectiveTransform(img, pts):
    rect = sortPoint(pts)
    tl, tr, br, bl = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tl[0] - tr[0]) ** 2) + ((tl[1] - tr[2]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # destination points
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    
    # perspective matrix
    M = cv.getPerspectiveTransform(rect, dst)
    warped = cv.warpPerspective(img, M, (maxWidth, maxHeight))

    return warped
