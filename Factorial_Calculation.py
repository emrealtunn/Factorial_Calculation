while True:
    try:
        sayi=int(input("Faktöriyelini öğrenmek istediğiniz bir sayıyı giriniz:"))
        carpma=1
        for i in range(sayi,0,-1):                        
            carpma=carpma*i
        print("Girdiğiniz sayı {}, faktoriyeli {} sayısıdır.".format(sayi,carpma))
    except ValueError :
        print("Lütfen sayı giriniz !")
