import cv2
import numpy as np

# print("Hi")

# 1. Image File
# img = cv2.imread("Resources/prabha statement page.PNG")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# 2. Video File
# cap = cv2.VideoCapture("Resources/video.mp4")
# while True:
#     success, imge=cap.read()
#     cv2.imshow("videoimg",imge)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# 3. Web Cam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480) #
# # cap.set(10,100) # Increase Breightness id 10
# while True:
#     success, imge=cap.read()
#     cv2.imshow("videoimg",imge)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# 4. BASIC FUNCTION
# img = cv2.imread("Resources/prabha statement page.PNG")
# # img = cv2.imread("Resources/img.PNG")
# kernal=np.ones((5,5),np.uint8)
#
# imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)
# imgCanny2 = cv2.Canny(img,150,200)
# imgDialation = cv2.dilate(imgCanny2,kernal,iterations=1)
# imgeroded = cv2.erode(imgDialation,kernal,iterations=1)
#
# cv2.imshow("Grey Image",imgGrey)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny2)
# cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgeroded)
#
# cv2.waitKey(0)

# 5. RESIZING & CROPPING OPECV CONVENTIONS
# img = cv2.imread("Resources/img.PNG")
# print(img.shape) #(440, 429, 3) 440-height 429-width 3-channel BGR
# imgResize = cv2.resize(img,(200,200))
# imgResize2 = cv2.resize(img,(1000,500)) #width and Height
# imgCropped=img[0:200,200:500] #height then width
#
# cv2.imshow("Image",img)
# cv2.imshow("Resized Image",imgResize)
# cv2.imshow("Cropped Image",imgCropped)
#
# cv2.waitKey(0)

# 6. SHAPES & TEXTS
# img = cv2.imread("Resources/img.PNG")
# # img = np.zeros((512,512,3),np.uint8)
# # img[:]= 250,0,0
# # img[100:200,100:200]= 250,0,0
# # cv2.line(img,(0,0),(200,200),(0,250,0),2)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2) #img.shape[0] -hight and img.shape[1] -width
# cv2.rectangle(img,(0,0),(250,300),(0,0,255),1)
# # cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED)
# cv2.circle(img,(200,300),50,(255,255,0),2)
# cv2.putText(img,"PRABHA",(0,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),2)
#
# cv2.imshow("Image",img)
# cv2.waitKey(0)

# 7. WARP PRESPECTIVE
# img = cv2.imread("Resources/img3.PNG")
#
# width,height = 750,355
# pts1 = np.float32([[36,125],[336,16],[132,241],[453,95]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#
# cv2.imshow("Image",img)
# cv2.imshow("Image Out",imgOutput)
# cv2.waitKey(0)

# 8. JOINING IMAGES

