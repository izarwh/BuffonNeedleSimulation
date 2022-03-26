from turtle import *
from random import *


#note, satuan tidak diperhatikan selagi panjang kertas, jarak garis, panjang korek berada dalam satuan yang sama
ht()
speed(0)
color('green')
#l dikali 10 untuk panjang korek
l=45
lcm = 4,5*100/2.5
#d dikali 10 untuk jarak antar garis
d=50
dcm = 50*10/2.5
#1 pixel = 2,5 cm
#luas daerah = 25 cm * 100
p=250
pcm = 25*100/2.5

drops = 100  # increase number of drops for better approximation
hits = 0    # hits counter

# menggambar garis dengan koordinat memulai menggambar garis -90
#tingginya 160 sehinga memiliki panjang area 250 yang mana 250/d = 5 garis
# for i in range(-90,160,d): 
for i in range(-90,160,d):
    pu()
    setpos(-100, i)
    pd()
    fd(250) # length of line 

# throw needles
color('black')
for j in range(drops):
    pu()
    goto(randrange(-100, 150), randrange(-50,150)) 
    #randrange pertama dari -100 sampai 150 karena panjang garis 250
    #randrage ke dua dari -50 sampai 150 karena tidak akan ada 
    #korek yang keluar dari garis terbawah, garis terbawah == batas kertas
    y1 = ycor() #saat garis digambarkan
    seth(360*random())
    pd(); fd(l)    #menggambar korek
    y2 = ycor() #saat garis selesai digambar

    if y1//20 != y2//20:    # decisive test: if it is a hit then ...
        hits += 1       # increase the hits counter by 1

hasil = (2 *(l/d) *(drops / hits))
print("yang terkena garis = "+ str(hits))
print("phi = "+str(hasil))
phieks = 3.1428
galat = (1-(phieks/hasil))*100
if (galat < 0):
  galat=galat*(-1)
print(galat)