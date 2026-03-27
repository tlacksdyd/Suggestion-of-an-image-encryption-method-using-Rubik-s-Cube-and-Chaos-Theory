random_key= ['B', 'U', 'L']

import numpy as np
from PIL import Image


Encryptionkey= random_key
 
DecryptionKey = Encryptionkey[::-1]

print(DecryptionKey)

def descramble(li, DecryptionKey):
    Block1 = li[0:9]
    Block2 = li[9:18]
    Block3 = li[18:27]
    Block4 = li[27:36]
    Block5 = li[36:45]
    Block6 = li[45:54]

    for i in range(len(DecryptionKey)):
        i = 0
        i += 1
        F = 'F'
        B = 'B'
        U = 'U'
        D = 'D'
        R = 'R'
        L = 'L'

        if F in DecryptionKey:
                Block1[6:9] = Block4[0], Block4[3], Block4[6]
                Block4[0], Block4[3], Block4[6] = Block5[2], Block5[1], Block5[0] 
                Block5[2], Block5[1], Block5[0] = Block2[8], Block2[5], Block2[2]
                Block2[8], Block2[5], Block2[2]  = Block1[6:9]
                Block3[7], Block3[8], Block3[5], Block3[2], Block3[1] = Block3[3], Block3[6], Block3[7], Block3[8], Block3[5] 
                Block3[6], Block3[3], Block3[0] = Block3[0:3]
                
                
               
                

        if B in DecryptionKey:
                Block1[2], Block1[1], Block1[0] = Block4[8], Block4[5], Block4[2]
                Block4[8], Block4[5], Block4[2] = Block5[6:9]
                Block5[6:9] = Block2[0], Block2[3], Block2[6]
                Block2[0], Block2[3], Block2[6] = Block1[0:3]
                Block6[2], Block6[1], Block6[5], Block6[8], Block6[7] = Block6[0], Block6[3], Block6[1], Block6[2], Block6[5] 
                Block6[0], Block6[3], Block6[6] = Block6[6:9]
                
                
                
                
                
                
        if U in DecryptionKey:
                Block2[0:3] = Block6[8], Block6[7], Block6[6]
                Block6[8], Block6[7], Block6[6] = Block4[0:3]
                Block4[0:3] = Block3[0:3]
                Block3[0:3]= Block2[0:3]
                Block1[7], Block1[8], Block1[5], Block1[2], Block1[1] = Block1[3], Block1[6], Block1[7], Block1[8], Block1[5]
                Block1[6], Block1[3], Block1[0] = Block1[0:3]
                
                
        if D in DecryptionKey:
                Block4[6:9] = Block6[2], Block6[1], Block6[0]
                Block6[0:3] = Block2[6], Block2[7], Block2[8] 
                Block3[6:9] = Block4[6:9] 
                Block2[6:9] = Block3[6:9]
                Block5[7], Block5[8], Block5[5], Block5[2], Block5[1]=Block5[3], Block5[6], Block5[7], Block5[8], Block5[5]
                Block5[6], Block5[3], Block5[0] = Block5[0:3]
                 
                
                
                
                 
                
        if R in DecryptionKey:
                Block3[2], Block3[5], Block3[8] = Block1[2], Block1[5], Block1[8]
                Block1[2], Block1[5], Block1[8] = Block6[2], Block6[5], Block6[8]
                Block6[2], Block6[5], Block6[8] = Block5[2], Block5[5], Block5[8]
                Block5[2], Block5[5], Block5[8] = Block3[2], Block3[5], Block3[8]
                Block4[7], Block4[8], Block4[5], Block4[2], Block4[1] = Block4[3], Block4[6], Block4[7], Block4[8], Block4[5]
                Block4[6], Block4[3], Block4[0] = Block4[0:3]
                
                
                
                
                
            
        if L in DecryptionKey:
                Block3[0], Block3[3], Block3[6] = Block1[0], Block1[3], Block1[6]
                Block1[0], Block1[3], Block1[6] = Block6[0], Block6[3], Block6[6]
                Block6[0], Block6[3], Block6[6] = Block5[0], Block5[3], Block5[6]
                Block5[0], Block5[3], Block5[6] = Block3[0], Block3[3], Block3[6]
                Block2[1], Block2[0], Block2[3], Block2[6] = Block2[5:9]
                Block2[1], Block2[2], Block2[5], Block2[8] = Block2[0:4]
                
                
                
                
                  

    return Block1 + Block2 + Block3 + Block4 + Block5 + Block6

img = Image.open('C:\\Users\\User\\Desktop\\학술제 코딩\\encrypted_image.bmp')
imgarr = np.array(img)


newlist = []

for i in range(imgarr.shape[0]):
    for j in range(imgarr.shape[1]):
        newlist.append(imgarr[i][j])



for k in range(0, len(newlist), 54):
    newlist[k:k+54]= descramble(newlist[k:k+54], DecryptionKey)
    


final = []

for i in newlist:
    final.append(i)

finall= np.array(final).reshape((1080, 1920))

img = Image.fromarray(finall)

img.show()

img.save('decrypted_image.bmp', "BMP")




