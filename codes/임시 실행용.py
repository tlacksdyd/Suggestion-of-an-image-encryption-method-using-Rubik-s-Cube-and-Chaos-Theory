routine = int(input('몇번 돌릴래?'))
random_key = []
import random
for i in range (1,routine+1):
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


def scramble(li, random_key):
    Block1 = li[0:9]
    Block2 = li[9:18]
    Block3 = li[18:27]
    Block4 = li[27:36]
    Block5 = li[36:45]
    Block6 = li[45:54]

    for i in range(routine):
        i = 0
        i += 1
        F = 'F'
        B = 'B'
        U = 'U'
        D = 'D'
        R = 'R'
        L = 'L'

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

    return Block1, Block2, Block3, Block4, Block5, Block6


img = Image.open('./image.jpg')
imgarr = np.array(img)

print(imgarr.shape[0])

newlist = []

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        newlist.append(imgarr[i][j][1])

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


cutlist = list_chunk(newlist, 54)

cutlist = []

for i in range(0, len(newlist), 9):
    cutlist.append(newlist[i:i + 9])
    
cutlist_f = sum(cutlist, [])

for k in range(0, len(cutlist), 54):
    cutlist_f[k:k+54]= scramble(cutlist_f[k:k+54], random_key)
    


final = []

for i in cutlist_f:
        final.extend(i)

final = np.array(final).reshape((1920, 1080))

img = Image.fromarray(final, 'L')

img.show()
