import cv2
import numpy as np

def nothing(x):
    pass


image = cv2.imread('./images/street.jpg')
image = cv2.resize(image, (400, 400))


cv2.namedWindow('Masked Image')

# Add sliders for mask position and size and blur
cv2.createTrackbar('X', 'Masked Image', 200, 400, nothing)
cv2.createTrackbar('Y', 'Masked Image', 200, 400, nothing)
cv2.createTrackbar('Size', 'Masked Image', 100, 200, nothing)
cv2.createTrackbar('Blur', 'Masked Image', 1, 50, nothing)

while True:
    # Get current positions of sliders
    cx = cv2.getTrackbarPos('X', 'Masked Image')
    cy = cv2.getTrackbarPos('Y', 'Masked Image')
    size = cv2.getTrackbarPos('Size', 'Masked Image')
    blur_val = cv2.getTrackbarPos('Blur', 'Masked Image')

    # blur kernel size is odd and at least 1
    k = blur_val if blur_val % 2 == 1 else blur_val + 1
    k = max(1, k)
   
    
    mask = np.zeros(image.shape[:2], dtype='uint8')
    

    cv2.rectangle(mask, 
                 (max(0, cx - size), max(0, cy - size)),  # cv2.rectangle(mask, pt1, pt2, color, thickness)
                 (min(400, cx + size), min(400, cy + size)), 
                 255, -1)

    # Blur the entire image
    blurred = cv2.blur(image, (k, k), 0)
    
   
    # Take the blurred image as base
    final = blurred.copy()
    # Put the original image where the mask is
    final[mask == 255] = image[mask == 255]
    
    # Show result
    cv2.imshow('Masked Image', final)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cv2.destroyAllWindows()





