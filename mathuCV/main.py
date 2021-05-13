import cv2
import numpy as np

image = cv2.imread("greenThingsRemastered.png")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_range = np.array([40, 0, 0])
upper_range = np.array([70, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imwrite("maskog.jpg", mask)

# =======================================================
# read image
img = cv2.imread("maskog.jpg")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]

# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
i = 0
for cntr in contours:
    x, y, w, h = cv2.boundingRect(cntr)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    print("x,y,w,h:", x, y, w, h)
    if w*h > 20:
        i = i+1
    print(str(i))
# save resulting image

result = cv2.putText(result, str(i), (0,50), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0),thickness=3 )
cv2.imwrite('two_blobs_result.jpg', result)

# show thresh and result
cv2.imshow("bounding_box", result)
cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()