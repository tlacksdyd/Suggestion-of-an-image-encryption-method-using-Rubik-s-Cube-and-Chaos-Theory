# RAW 사진 파일 화면 출력
from tkinter import *

## 함수 선언 부분 ##
def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.readㄹ(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# 파일 --> 메모리
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw             #내가 쓸 자료: C:\Users\User\Downloads\Images\RAW\LENA256
loadImage(filename)

# 메모리 --> 화면 
displayImage(inImage)

canvas.pack()
window.mainloop()











# 엑셀 파일의 셀에 색상을 지정하는 코드 완성 - 이미지 변경
from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture06.gif')
h = photo.height()
w = photo.width()

photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/picture06_art.xlsx')
worksheet = workbook.add_worksheet('photoRGB')

worksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    worksheet.set_row(i, 9.5)  # 약 0.35

for i in range(w) :
    for k in range(h) :
        hexR = hex(photoR[i][k])
        hexG = hex(photoG[i][k])
        hexB = hex(photoB[i][k])
        hexStr = '#'
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]

        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

workbook.close()
print('Save. OK~')










# 넘파이를 활용하여 영상 변환하기

import numpy as np
from tkinter import *

## 함수 선언부
def displayImage(imageR, imageG, imageB) :
    rgbString = ""
    for i in range(0, h) :
        tmpString = ""
        for k in range(0, w) :
            dataR = imageR[k][i]
            dataG = imageG[k][i]
            dataB = imageB[k][i]
            tmpString += "#%02x%02x%02x " % (dataR, dataG, dataB) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

## 전역 변수부
window = None
canvas = None
w, h = 0, 0
photoR, photoG, photoB = None, None, None # 2차원 넘파이 배열

## 메인 코드부
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture24.gif')
h = photo.height()
w = photo.width()
window.title("GIF 사진 처리")              
canvas = Canvas(window, height = h, width = w)
paper = PhotoImage(height = h, width = w)
canvas.create_image((w/2, h/2), image = paper, state = "normal")

photoR=np.empty((w, h), dtype=np.uint8)
photoG=np.empty((w, h), dtype=np.uint8)
photoB=np.empty((w, h), dtype=np.uint8)

## (1)원본 추출 및 출력
for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b
displayImage(photoR, photoG, photoB)

## (2) 반전 처리 및 출력
photoR = 255 - photoR
photoG = 255 - photoG
photoB = 255 - photoB
displayImage(photoR, photoG, photoB)

## (3) 회색영상 처리 및 출력
photoRGB =  (photoR.astype(np.uint16) + photoG.astype(np.uint16)  + photoB.astype(np.uint16) )
photoRGB =  photoRGB / 3
photoRGB = photoRGB.astype(np.uint8)
photoR = photoG = photoB = photoRGB
displayImage(photoR, photoG, photoB)

## (4) 흑백 처리 및 출력
photoR = np.where(photoR < 128, 0, 255)
photoG = np.where(photoR < 128, 0, 255)
photoB = np.where(photoR < 128, 0, 255)
displayImage(photoR, photoG, photoB)

canvas.pack()
window.mainloop()
