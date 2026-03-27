import numpy as np
from PIL import Image
import numpy as np



#원본 이미지 열기(인식)
img1= Image.open('C:\\Users\\User\\Desktop\\학술제 코딩\\cube_original_image.jpg') #파일 경로 or 이름
img1.show()

#이미지를 np.array 로 변환
imgarr1 = np.array(img1)


oldlist=[]

for i in range(imgarr1.shape[0]):
    for j in range(imgarr1.shape[1]):
        oldlist.append(imgarr1[i][j])


img2= Image.open('C:\\Users\\User\\Desktop\\학술제 코딩\\cube_encrypted_image.jpg')
img2.show()

imgarr2 = np.array(img2)

newlist=[]

for i in range(imgarr2.shape[0]):
    for j in range(imgarr2.shape[1]):
        newlist.append(imgarr2[i][j])



B=oldlist

A=newlist

#NPCR 공식
D=0
for i in range(len(A)):
    if A[i] != B[i]:
        D += 1
NPCR = (D*100)/(1920*1080)

print('NPCR =', NPCR)



#UACI 공식 표현
E=0
for i in range(len(A)):
    if int(A[i])-int(B[i]) >= 0:
        E =E + (int(A[i])-int(B[i]))
    if int(A[i])-int(B[i]) < 0:
        E = E - (int(A[i])-int(B[i]))
UACI = (E*100)/(1920*1080*255)
#UACI 값 출력
print('UACI = ', UACI)
