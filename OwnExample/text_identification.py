import cv2
import pytesseract

img = cv2.imread("texts.PNG")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(threshold_otsu, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img1 = img.copy()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cropped = img1[y:y + h, x:x + w]
    text = pytesseract.image_to_string(cropped)
    if text == "Apple":
        rect = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imwrite("new_Apple.PNG", img1)
