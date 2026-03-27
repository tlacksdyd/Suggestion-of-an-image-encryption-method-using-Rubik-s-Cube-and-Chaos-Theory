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

import numpy as np
from PIL import Image


# print(newlist)
# 이미지 파일을 픽셀별로 나누어서 차례로 1차원 리스트로 배열하기(grayscale 0~255까지의 색 값으로)

img = Image.open('image.jpg')
imgarr = np.array(img)

print(imgarr.shape[0])

newlist = []

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        newlist.append(imgarr[i][j][1])


def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


list_splited = list_chunk(newlist, 54)

#print("분할 후 : ", list_splited)(잠시보류)


#temp global 변수에 list_splited(54개씩 한 묶음) 할당하기-->dynamic 변수 생성 
for k in range(0,120*320):
    globals()['temp_{}'.format(k)] = list_splited[k]


#54개씩 할당된 temp변수를 또 9개씩 나누기
for k in range(0,120*320):
    globals()['temp_{}'.format(k)] = list_chunk(list_splited[k], 9)
    
for k in range(0,120*320):
    Block1=globals()['temp_{}'.format(k)][0] 
    Block2=globals()['temp_{}'.format(k)][1] 
    Block3=globals()['temp_{}'.format(k)][2] 
    Block4=globals()['temp_{}'.format(k)][3]
    Block5=globals()['temp_{}'.format(k)][4] 
    Block6=globals()['temp_{}'.format(k)][5] 


    def scramble():
        for i in range (key_length):
            i=0
            i=i+1
            F='F'
            B='B'
            U='U'
            D='D'
            R='R'
            L='L'
            if F in random_key:
                Block3[0:3] = Block3[6], Block3[3], Block3[0] 
                Block3[3], Block3[6], Block3[7], Block3[8], Block3[5] = Block3[7], Block3[8], Block3[5], Block3[2], Block3[1]
                Block1[6:9] = Block2[8], Block2[5], Block2[2] 
                Block2[8], Block2[5], Block2[2] = Block5[2], Block5[1], Block5[0]
                Block5[2], Block5[1], Block5[0] = Block4[0], Block4[3], Block4[6]
                Block4[0], Block4[3], Block4[6]= Block1[6:9]
                
            if B in random_key:
                Block6[6:9] = Block6[0], Block6[3], Block6[6]
                Block6[0], Block6[3], Block6[1], Block6[2], Block6[5] =  Block6[2], Block6[1], Block6[5], Block6[8], Block6[7]
                Block1[0:3]=Block2[0], Block2[3], Block2[6]
                Block2[0], Block2[3], Block2[6]=Block5[6:9]
                Block5[6:9]= Block4[8], Block4[5], Block4[2]
                Block4[8], Block4[5], Block4[2]= Block1[2], Block1[1], Block1[0]
                
            if U in random_key:
                Block1[0:3]= Block1[6], Block1[3], Block1[0]
                Block1[3], Block1[6], Block1[7], Block1[8], Block1[5] = Block1[7], Block1[8], Block1[5], Block1[2], Block1[1]
                Block2[0:3]=Block3[0:3]
                Block3[0:3]=Block4[0:3]
                Block4[0:3]=Block6[8], Block6[7], Block6[6]
                Block6[8], Block6[7], Block6[6]=Block2[0:3]
                
            if D in random_key:
                Block5[0:3]= Block5[6], Block5[3], Block5[0]
                Block5[3], Block5[6], Block5[7], Block5[8], Block5[5] = Block5[7], Block5[8], Block5[5], Block5[2], Block5[1]
                Block3[6:9] = Block2[6:9]
                Block4[6:9] = Block3[6:9]
                Block2[6], Block2[7], Block2[8] = Block6[0:3]
                Block6[2], Block6[1], Block6[0] = Block4[6:9]
                
            if R in random_key:
                Block4[0:3] = Block4[6], Block4[3], Block4[0]
                Block4[3], Block4[6], Block4[7], Block4[8], Block4[5] = Block4[7], Block4[8], Block4[5], Block4[2], Block4[1]
                Block3[2], Block3[5], Block3[8]=Block5[2], Block5[5], Block5[8]
                Block5[2], Block5[5], Block5[8]=Block6[2], Block6[5], Block6[8]
                Block6[2], Block6[5], Block6[8]=Block1[2], Block1[5], Block1[8]
                Block1[2], Block1[5], Block1[8]=Block3[2], Block3[5], Block3[8]
            
            if L in random_key:
                Block2[0:4]=Block2[1], Block2[2], Block2[5], Block2[8]
                Block2[5:9] = Block2[1], Block2[0], Block2[3], Block2[6]
                Block3[0], Block3[3], Block3[6]=Block5[0], Block5[3], Block5[6]
                Block5[0], Block5[3], Block5[6]=Block6[0], Block6[3], Block6[6]
                Block6[0], Block6[3], Block6[6]=Block1[0], Block1[3], Block1[6]
                Block1[0], Block1[3], Block1[6]=Block3[0], Block3[3], Block3[6]   
    
    scramble()
    
    globals()['final_list_bef_{}'.format(k)] = Block1 + Block2 + Block3 + Block4 + Block5 +Block6
    

for r in range(0, 120*320): 
    final_list = []
    final_list = final_list.extend(globals()['final_list_bef_{}'.format(r)])
    
    
    
   
#final_list를 다시 np.array로 변환
ret = np.array(final_list).reshape((1920, 1080))


#이미지 재조합 후 출력
pil_image=Image.fromarray(ret)
pil_image.show()





