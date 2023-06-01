print("""
***********************

xow gelmisizinz




***********************
""")

import random
import time



rastegle_sayi=random.randint(1,100)
texmin_haqqi=7

while True:
    tahmin = int(input("texmininiz:"))
    
    if(rastegle_sayi == tahmin ):
        print("sorgulanir")
        time.sleep(1)
        print("tebrikler")
        break
    elif(rastegle_sayi < tahmin):
         print("sorgulanir")
         time.sleep(1)
         print("daha asagi sayi girin")
         texmin_haqqi -= 1
    
    else:
        print("sorgulanir")
        time.sleep(1)
        print("daha boyuk say yazin")
        texmin_haqqi -= 1
    if(texmin_haqqi == 0):
        print("sizin haqqiniz qalmadi")
        print("sayimiz",rastegle_sayi)
        break          
    