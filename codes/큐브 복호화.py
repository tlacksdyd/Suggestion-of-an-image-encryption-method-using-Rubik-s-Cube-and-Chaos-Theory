NPCR_list=[]
UACI_list=[]

for i in range(int(input('몇 번 반복하실건가요?: '))):
    i=0
    i+=1
    #사용자가 입력한 암호화 키 길이수를 갖춘 랜덤 키 생성
    routine = int(input('암호화 키 길이를 입력하시오: '))
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
            
    Decryptionkey = random_key[::-1]

    #생성된 복호화 키 프린트
    print(random_key)
    print(Decryptionkey)


    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image

    #random_key에 따라 픽셀 섞어주는 함수 정의
    def scramble(li, random_key):
        list1 = li
        list2 = li

    
        for i in range(routine):
            i = 0
            F = 'F'
            B = 'B'
            U = 'U'
            D = 'D'
            R = 'R'
            L = 'L'

            if U in random_key:
                list2[6:9] = list1[17], list1[14], list1[11]
                list2[27], list2[30], list2[33] = list1[6:9]
                list2[36:39] = list1[33], list1[30], list1[27]
                list2[11], list2[14], list2[17] = list1[36:39]
                list2 [18:21] = list1[24], list1[21], list1[18]
                list2[20], list2[23], list2[26] = list1[18:21]
                list2[24:27] = list1[26], list1[23], list1[20]
                list2[18], list2[21], list2[24] = list1[24:27]

            if D in random_key:
                list2[0:3] = list1[15], list1[12], list1[9]
                list2[29], list2[32], list2[35] = list1[0:3]
                list2[42:45] = list1[29], list1[32], list1[35]
                list2[9], list2[12], list2[15] = list1[42:45]
                list2[51:54] = list1[45], list1[48], list1[51]
                list2[53], list2[50], list2[47] = list1[51:54]
                list2[45:48] = list1[47], list1[50], list1[53]
                list2[51], list2[48], list2[45] = list1[45:48]


            if L in random_key:
                list2[24], list2[21], list2[18] = list1[42], list1[39], list1[36]
                list2[0], list2[3], list2[6] = list1[18], list1[21], list1[24]
                list2[45], list2[48], list2[51] = list1[0], list1[3], list1[6]
                list2[36], list2[39], list2[42] = list1[45], list1[48], list1[51]
                list2[17], list2[14], list2[11] = list1[15], list1[16], list1[17]
                list2[9], list2[10], list2[11] = list1[11], list1[14], list1[17]
                list2[15], list2[12], list2[9] = list1[9], list1[10], list1[11]
                list2[17], list2[16], list2[15] = list1[15], list1[12], list1[9]

            if B in random_key:
                list2[51:54] = list1[11], list1[10], list1[9]
                list2[30], list2[29], list2[28] = list1[51:54]
                list2[18:21] = list1[27:30]
                list2[9:12] = list1[18:21]
                list2[0:3] = list1[0], list1[3], list1[6]
                list2[2], list2[5], list2[8] = list1[0:3]
                list2[6:9] = list1[2], list1[5], list1[8]
                list2[0], list2[3], list2[6] = list1[6:9]

            if R in random_key:
                list2[26], list2[23], list2[20] = list1[44], list1[41], list1[38]
                list2[8], list2[5], list2[2] = list1[26], list1[23], list1[20]
                list2[47], list2[50], list2[53] = list1[2], list1[5], list1[8]
                list2[38], list2[41], list2[44] = list1[47], list1[50], list1[53]
                list2[33], list2[30], list2[27] = list1[33:36]
                list2[27:30] = list1[33], list1[30], list1[27]
                list2[29], list2[32], list2[35] = list1[27:30]
                list2[33:36] = list1[35], list1[32], list1[29]

            if F in random_key:
                list2[24:27] = list1[15:18]
                list2[33:36] = list1[24:27]
                list2[45], list2[46], list2[47] = list1[35], list1[34], list1[33]
                list2[15], list2[16], list2[17] = list1[47], list1[46], list1[45]
                list2[36:39] = list1[42], list1[39], list1[36]
                list2[44], list2[41], list2[38] = list1[38], list1[37], list1[36]
                list2[42], list2[43], list2[44] = list1[44], list1[41], list1[38]
                list2[36], list2[39], list2[42] = list1[42], list1[43], list1[44]
                
            i+=1  
        #섞인 이미지 값 반환
        return list2


    #원본 이미지 열기(인식)     
    img = Image.open('C:\\Users\\User\\Desktop\\학술제 코딩\\image.bmp') #문자열 안에 파일 경로 입력
    imgarr = np.array(img) #이미지를 array 배열로 변형

    #원본 이미지를 리스트로 변환-->oldlist에 저장
    oldlist=[]


    for i in range(imgarr.shape[0]): 
        for j in range(imgarr.shape[1]): 
            oldlist.append(imgarr[i][j][1])
            

    #암호화 후 이미지를 생성하기 위해 새로운 리스트 생성(아직 원본 이미지가 담겨있는 list)
    newlist = []

    for i in range(imgarr.shape[0]):
        for j in range(imgarr.shape[1]):
            newlist.append(imgarr[i][j][1])
            
        
    #newlist 에 담긴 원본 이미지 픽셀값들을 scramble 함수를 이용하여 섞어주기
    for k in range(0, len(newlist), 54):
        newlist[k:k+54]= scramble(newlist[k:k+54], random_key)

    #섞인 newlist를 final변수에 1080*1920으로 reshape 해서 넣어주기
    final= np.array(newlist).reshape((1080, 1920))

    img = Image.fromarray(final)
    img.show()

    #이미지 저장(BMP 파일)
    img.save('encrypted_image.bmp', "BMP")



    #여기부터는 NPCR과 UACI 출력 코드

    #B는 암호화전 이미지 픽셀값을 담은 리스트
    B=oldlist

    finall=[]

    for i in newlist:
        finall.append(i)

    #A는 암호화 후 이미지 픽셀값을 담은 리스트
    A=newlist

    #NPCR 공식 표현
    D=0
    for i in range(len(A)):
        if A[i] != B[i]:
            D += 1
    NPCR = (D*100)/(1920*1080)

    #NPCR값 출력
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

  

    NPCR_list.append(NPCR)
    UACI_list.append(UACI)
    
print(NPCR_list)
print(UACI_list)
  
  
plt.plot(NPCR_list)
plt.show()

plt.plot(UACI_list)
plt.show()
    


avg1= sum(NPCR_list) / len(NPCR_list)
print('average of NPCR: ', avg1)

avg2 = sum(UACI_list) / len(UACI_list)
print('average of UACI: ', avg2)


