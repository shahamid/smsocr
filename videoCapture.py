import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cam = cv2.VideoCapture(0)

print(cam)
i=1

if not (cam.isOpened()):
    print("Could not open video device")
else:
    while cam.isOpened() and i<500:
        result, image = cam.read()

        if result:
            cv2.imshow("cam", image)
            text = pytesseract.image_to_string(image, lang="eng+fas")
            if text != "":
                print(text)            
            cv2.waitKey(10)
        else:
            print(result)
        
        i += 1
    
cam.release()
cv2.destroyAllWindows()
