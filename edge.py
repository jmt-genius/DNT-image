import cv2

image = cv2.imread('duck.jpeg', cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

cv2.imshow('Sketched Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
