#for_function 파일에서 keygen 함수 불러오기
from for_function import keygen as kg
import numpy as np
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

NPCR_list=[]
UACI_list=[]
r=[]


b=float(input('3이상 4미만의 r 값을 입력하세요: '))

#원본 이미지 열기(인식)
img = Image.open('C:/Users/User/Desktop/학술제 코딩/image.bmp') #파일 경로 or 이름
img.show()
#img.show()

#이미지를 np.array 로 변환
imgarr = np.array(img)

#원본 이미지의 픽셀값이 리스트로 담길 oldlist
oldlist=[]

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        oldlist.append(imgarr[i][j][1])
    

#이미지 세로길이, 가로 길이 정의
height = imgarr.shape[0]
width= imgarr.shape[1]

x_value = 0.6
r_value = b

#카오스 키 생성--> 여기서 0.01, 3.95는 임의의값
key=kg(x_value, r_value, height*width)

        
        
scrambledlist=[]

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        scrambledlist.append(imgarr[i][j][1])

z=0
for i in range(1920*1080):
    scrambledlist[i]=(oldlist[i]*key[z])%255
    z+=1
    
            
temp=[]

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        temp.append(imgarr[i][j][1])
    
z=0
for i in range(1920*1080):
    temp[i]=(oldlist[i]*key[z])/255
    z+=1
    


#섞인 이미지인 newlist를 1080*1920 사이즈로 조정후 final에 저장
final= np.array(scrambledlist).reshape((1080, 1920))

img1 = Image.fromarray(final)
img1.show()
#img1.show()


    
    
#여기부터 NPCR, UACI 코드

#B는 암호화 전 이미지 픽셀값을 담은 리스트 
B=oldlist

A=scrambledlist
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

    
finalD = []
for i in scrambledlist:
    finalD.append(i)
    



z=0
for i in range(1920*1080):
    try:
        finalD[i] = (temp[i]*255+scrambledlist[i])/key[z]
        z+=1

    except ZeroDivisionError:
        finalD[i] = oldlist[i]
        z+=1



for_showing= np.array(finalD).reshape((1080, 1920))



imgn = Image.fromarray(for_showing)
imgn.show()

#imgn.show()

NPCR_list.append(NPCR)
UACI_list.append(UACI)

r.append(r_value)
        
   
      
"""  
plt.plot(r,NPCR_list)
plt.show()

plt.plot(r, UACI_list)
plt.show()
"""