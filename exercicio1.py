Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> imagemcarregada = cv2.imread("gato.jpeg",0)
>>> cv2.imshow("imagemcarregada",imagemcarregada)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    cv2.imshow("imagemcarregada",imagemcarregada)
cv2.error: OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\highgui\src\window.cpp:352: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

>>> cv2.waitkey(0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cv2.waitkey(0)
AttributeError: module 'cv2.cv2' has no attribute 'waitkey'
>>> cv2.destroyAllWindows()
>>> 
