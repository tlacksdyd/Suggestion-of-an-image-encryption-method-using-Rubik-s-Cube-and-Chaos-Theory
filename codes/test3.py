#numpy 라이브러리 임포트해오기
#pillow로 이미지 불러오기

import numpy as np
from PIL import Image

#랜덤 키 생성, 사용자에게 키 길이만입력받음

key_length = int(input('몇번 돌릴래?'))
random_key = []
import random
for i in range (1,key_length+1):
    num= random.randrange(1, 7)
    if num==1:
        random_key.append('U')
    if num==2:
        random_key.append('R')
    if num==3:
        random_key.append('L')
    if num==4:
        random_key.append('B')
    if num==5:
        random_key.append('D')
    if num==6:
        random_key.append('F')

print(random_key)

#큐브 리스트 지정

Block1=[1,2,3,4,5,6,7,8,9]
Block2=[10,11,12,13,14,15,16,17,18]
Block3=[19,20,21,22,23,24,25,26,27]
Block4=[28,29,30,31,32,33,34,35,36]
Block5=[37,38,39,40,41,42,43,44,45]
Block6=[46,47,48,49,50,51,52,53,54]






routine = int(input())

#리스트 섞는 코드(수정 해야함), 아직 실행이 안됨
def scramble():
    for i in range (routine):
        i=0
        i+=1
        F='F'
        B='B'
        U='U'
        D='D'
        R='R'
        L='L'
        if F in random_key:
            Block3[0:4], Block3[5:9] = Block3[6], Block3[3], Block3[0], Block3[7], Block3[1], Block3[8], Block3[5], Block3[2]
            Block1[6:9] = Block2[2], Block2[5], Block2[8] 
            Block2[2], Block2[5], Block2[8]= Block5[0:3]
            Block5[0:3] = Block4[0], Block4[3], Block4[6]
            Block4[0], Block4[3], Block4[6]= Block1[6:9]
            
        if B in random_key:
            Block1[0:3]=Block2[0], Block2[3], Block2[6]
            Block2[0], Block2[3], Block2[6]=Block5[6:9]
            Block5[6:9]= Block4[2], Block4[5], Block4[8]
            Block4[2], Block4[5], Block4[8]= Block1[0:3]
            Block6[0:4], Block6[5:9]=Block6[6], Block6[3], Block6[0], Block6[7], Block6[1], Block6[8], Block6[5], Block6[2]
            
        if U in random_key:
            Block1[0:4], Block1[5:9]=Block1[6], Block1[3], Block1[0], Block1[7], Block1[1], Block1[8], Block1[5], Block1[2]
            Block2[0:3]=Block3[0:3]
            Block3[0:3]=Block4[0:3]
            Block4[0:3]=Block6[8], Block6[7], Block6[6]
            Block6[8], Block6[7], Block6[6]=Block2[0:3]
            
        if D in random_key:
            Block5[0:4], Block5[5:9]=Block5[6], Block5[3], Block5[0], Block5[7], Block5[1], Block5[8], Block5[5], Block5[2]
            Block3[6:9]=Block2[6:9]
            Block4[6:9]=Block3[6:9]
            Block6[0:3]=Block2[8], Block2[7], Block2[6]
            Block6[2], Block6[1], Block6[0]=Block4[6:9]
            
        if R in random_key:
            Block4[0:4], Block4[5:9]=Block4[6], Block4[3], Block4[0], Block4[7], Block4[1], Block4[8], Block4[5], Block4[2]
            Block3[2], Block3[5], Block3[7]=Block5[2], Block5[5], Block5[8]
            Block5[2], Block5[5], Block5[8]=Block6[2], Block6[5], Block6[8]
            Block6[2], Block6[5], Block6[8]=Block1[2], Block1[5], Block1[8]
            Block1[2], Block1[5], Block1[8]=Block3[2], Block3[5], Block3[8]
        
        if L in random_key:
            Block2[0:4], Block2[5:9]=Block2[6], Block2[3], Block2[0], Block2[7], Block2[1], Block2[8], Block2[5], Block2[2]
            Block3[0], Block3[3], Block3[6]=Block5[0], Block5[3], Block5[6]
            Block5[0], Block5[3], Block5[6]=Block6[0], Block6[3], Block6[6]
            Block6[0], Block6[3], Block6[6]=Block1[0], Block1[3], Block1[6]
            Block1[0], Block1[3], Block1[6]=Block3[0], Block3[3], Block3[6]  



# print(newlist)
# 이미지 파일을 픽셀별로 나누어서 차례로 1차원 리스트로 배열하기(grayscale 0~255까지의 색 값으로)

img = Image.open('./image.jpg')
imgarr = np.array(img)

print(imgarr.shape[0])

newlist = []

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        newlist.append(imgarr[i][j][1])
        
