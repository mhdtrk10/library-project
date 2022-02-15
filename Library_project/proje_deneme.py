from kütüphane import *

print("""***********************************

Welcome to library project!

transactions;

1. Show books

2. Book inquiry

3. Add book

4. Delete book

5. Upgrade Oppression

press 'q' for quit.
***********************************""")

kütüphane = Kütüphane()

while True:
    işlem = input("your action:")

    if (işlem == "q"):
        print("have a nice day!")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        isim = input("Which book do you want ? ")
        print("Looking for book.. ")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("Name:")
        yazar = input("Writer:")
        yayınevi = input("Publisher:")
        tür = input("Type:")
        baskı = int(input("Opression"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Book being added..")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Book added..")


    elif (işlem == "4"):
        isim = input("Which book do you delete ?")

        cevap = input("Are you sure ? (Y/N)")
        if (cevap == "Y"):
            print("The book is being deleted..")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Book deleted..")


    elif (işlem == "5"):
        isim = input("Which book do you want to upgrade ?")
        print("Raising the pressure..")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Pressure is raised..")

    else:
        print("invalid transaction...")






















































