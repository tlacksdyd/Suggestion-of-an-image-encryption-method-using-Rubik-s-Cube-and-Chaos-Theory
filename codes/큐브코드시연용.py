import random

import numpy as np
from PIL import Image

NPCR_list = []
UACI_list = []


def encryption(li, random_key):
    list1 = li
    list2 = li

    for i in random_key:
        if i == "U":
            list2[6:9] = list1[17], list1[14], list1[11]
            list2[27], list2[30], list2[33] = list1[6:9]
            list2[36:39] = list1[33], list1[30], list1[27]
            list2[11], list2[14], list2[17] = list1[36:39]
            list2[18:21] = list1[24], list1[21], list1[18]
            list2[20], list2[23], list2[26] = list1[18:21]
            list2[24:27] = list1[26], list1[23], list1[20]
            list2[18], list2[21], list2[24] = list1[24:27]
        elif i == "D":
            list2[0:3] = list1[15], list1[12], list1[9]
            list2[29], list2[32], list2[35] = list1[0:3]
            list2[42:45] = list1[29], list1[32], list1[35]
            list2[9], list2[12], list2[15] = list1[42:45]
            list2[51:54] = list1[45], list1[48], list1[51]
            list2[53], list2[50], list2[47] = list1[51:54]
            list2[45:48] = list1[47], list1[50], list1[53]
            list2[51], list2[48], list2[45] = list1[45:48]
        elif i == "L":
            list2[24], list2[21], list2[18] = list1[42], list1[39], list1[36]
            list2[0], list2[3], list2[6] = list1[18], list1[21], list1[24]
            list2[45], list2[48], list2[51] = list1[0], list1[3], list1[6]
            list2[36], list2[39], list2[42] = list1[45], list1[48], list1[51]
            list2[17], list2[14], list2[11] = list1[15], list1[16], list1[17]
            list2[9], list2[10], list2[11] = list1[11], list1[14], list1[17]
            list2[15], list2[12], list2[9] = list1[9], list1[10], list1[11]
            list2[17], list2[16], list2[15] = list1[15], list1[12], list1[9]
        elif i == "B":
            list2[51:54] = list1[11], list1[10], list1[9]
            list2[30], list2[29], list2[28] = list1[51:54]
            list2[18:21] = list1[27:30]
            list2[9:12] = list1[18:21]
            list2[0:3] = list1[0], list1[3], list1[6]
            list2[2], list2[5], list2[8] = list1[0:3]
            list2[6:9] = list1[2], list1[5], list1[8]
            list2[0], list2[3], list2[6] = list1[6:9]
        elif i == "R":
            list2[26], list2[23], list2[20] = list1[44], list1[41], list1[38]
            list2[8], list2[5], list2[2] = list1[26], list1[23], list1[20]
            list2[47], list2[50], list2[53] = list1[2], list1[5], list1[8]
            list2[38], list2[41], list2[44] = list1[47], list1[50], list1[53]
            list2[33], list2[30], list2[27] = list1[33:36]
            list2[27:30] = list1[33], list1[30], list1[27]
            list2[29], list2[32], list2[35] = list1[27:30]
            list2[33:36] = list1[35], list1[32], list1[29]
        elif i == "F":
            list2[24:27] = list1[15:18]
            list2[33:36] = list1[24:27]
            list2[45], list2[46], list2[47] = list1[35], list1[34], list1[33]
            list2[15], list2[16], list2[17] = list1[47], list1[46], list1[45]
            list2[36:39] = list1[42], list1[39], list1[36]
            list2[44], list2[41], list2[38] = list1[38], list1[37], list1[36]
            list2[42], list2[43], list2[44] = list1[44], list1[41], list1[38]
            list2[36], list2[39], list2[42] = list1[42], list1[43], list1[44]

    return list2


#routine = int(input("Enter the number of routine: "))

encryption_key_length = int(input("Enter the length of encryption key: "))

keys = ['U', 'D', 'L', 'B', 'R', 'F']

# make key
encryption_key = []
for i in range(encryption_key_length):
    encryption_key.append(random.choice(keys))

decryption_key = encryption_key[::-1]

# load image to grayscale
img = Image.open('학술제 코딩\cube_original_image.jpg').convert('L')
img.save('save_original_image.jpg')

img.show()
print(img.size)
width, height = img.size
img = np.array(img)

img = img.reshape(54, -1)
img= np.transpose(img)

for i in range(img.shape[0]):
    img[i] = encryption(img[i], encryption_key)
    


img = img.reshape(height, width)

img = Image.fromarray(img)

img.show()
img.save('encrypted_image.jpg')

"""
newlist = []

z=0
for i in range(38400):
    for z in range(0, height*width-54, 54):
        newlist.append(img[z])
    z+=1
        
final= np.array(newlist).reshape((1080, 1920))

img1 = Image.fromarray(final)
img1.show()
"""