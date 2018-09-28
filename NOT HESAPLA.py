# Note Calculating #


from __future__ import division

print("Vize Sayısı En fazla: 2 olabilir.\nÖdev sayısı en fazla: 2 olabilir.")
vize_sayisi = input("Dersinizin kaç vizesi var? : ")
odev_sayisi = input("Dersinizin kaç ödevi var? : ")
gecme_notu = input("Dersin geçme notunu giriniz: ")

v = int(vize_sayisi)
os = int(odev_sayisi)
g = int(gecme_notu)
if (v == 1):
    if (os == 1):
        vize_yuzdesi = input("Vize yüzdesini giriniz(10,20 gibi) : ")
        odev_yuzdesi = input("Ödev yüzdesini giriniz(10,20 gibi) : ")
        vy = int(vize_yuzdesi)
        oy = int(odev_yuzdesi)
        final_yuzdesi = (100 - (vy + oy))
        print("Final Yüzdesi:", final_yuzdesi)
        vize_notu = input("Vize notunu giriniz : ")
        odev_notu = input("Ödev notunu giriniz : ")
        final_notu = input("Final notunu giriniz : ")
        vn = int(vize_notu)
        on = int(odev_notu)
        fn = int(final_notu)
        ders_notu = (vy / 100 * vn) + (oy / 100 * on) + (final_yuzdesi / 100 * fn)
        if (g >= 40):
            print("Geçme Notu 40, AA notu 85 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 40):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

        elif (g >= 50):

            print("Geçme Notu 50, AA notu 90 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 90):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")



    elif (os == 2):
        vize_yuzdesi = input("Vize yüzdesini giriniz(10,20 gibi) : ")
        odev1_yuzdesi = input("Ödev1 yüzdesini giriniz(10,20 gibi) : ")
        odev2_yuzdesi = input("Ödev2 yüzdesini giriniz(10,20 gibi) : ")
        vy = int(vize_yuzdesi)
        o1 = int(odev1_yuzdesi)
        o2 = int(odev2_yuzdesi)
        final_yuzdesi = (100 - (vy + o1 + o2))
        vize_notu = input("Vize notunu giriniz : ")
        odev1_notu = input("Ödev1 notunu giriniz : ")
        odev2_notu = input("Ödev2 notunu giriniz : ")
        final_notu = input("Final notunu giriniz : ")
        vn = int(vize_notu)
        o1_n = int(odev1_notu)
        o2_n = int(odev2_notu)
        fn = int(final_notu)
        ders_notu = vy / 100 * vn + o1 / 100 * o1_n + o2 / 100 * o2_n + final_yuzdesi / 100 * fn

        if (g >= 40):
            print("Geçme Notu 40, AA notu 85 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 40):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

        elif (g >= 50):

            print("Geçme Notu 50, AA notu 90 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 90):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

elif (v == 2):
    if (os == 1):
        vize1_yuzdesi = input("Vize1 yüzdesini giriniz(10,20 gibi) : ")
        vize2_yuzdesi = input("Vize2 yüzdesini giriniz(10,20 gibi) : ")
        odev_yuzdesi = input("Ödev yüzdesini giriniz(10,20 gibi) : ")
        v1y = int(vize1_yuzdesi)
        v2y = int(vize2_yuzdesi)
        oy = int(odev_yuzdesi)
        final_yuzdesi = (100 - (v1y + v2y + oy))
        vize1_notu = input("Vize1 notunu giriniz : ")
        vize2_notu = input("Vize2 notunu giriniz : ")
        odev_notu = input("Ödev notunu giriniz : ")
        final_notu = input("Final notunu giriniz : ")
        v1n = int(vize1_notu)
        v2n = int(vize2_notu)
        on = int(odev_notu)
        fn = int(final_notu)
        ders_notu = v1y / 100 * v1n + v2y / 100 * v2n + oy / 100 * on + final_yuzdesi / 100 * fn
        if (g >= 40):
            print("Geçme Notu 40, AA notu 85 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 40):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

        elif (g >= 50):

            print("Geçme Notu 50, AA notu 90 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 90):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")


    elif (os == 2):
        vize1_yuzdesi = input("Vize1 yüzdesini giriniz(10,20 gibi) : ")
        vize2_yuzdesi = input("Vize2 yüzdesini giriniz(10,20 gibi) : ")
        odev1_yuzdesi = input("Ödev1 yüzdesini giriniz(10,20 gibi) : ")
        odev2_yuzdesi = input("Ödev2 yüzdesini giriniz(10,20 gibi) : ")
        v1y = int(vize1_yuzdesi)
        v2y = int(vize2_yuzdesi)
        o1y = int(odev1_yuzdesi)
        o2y = int(odev2_yuzdesi)
        final_yuzdesi = (100 - (v1y + v2y + o1y + o2y))
        vize1_notu = input("Vize1 notunu giriniz : ")
        vize2_notu = input("Vize2 notunu giriniz : ")
        odev1_notu = input("Ödev1 notunu giriniz : ")
        odev2_notu = input("Ödev2 notunu giriniz : ")
        final_notu = input("Final notunu giriniz : ")
        v1n = int(vize1_notu)
        v2n = int(vize2_notu)
        on1 = int(odev1_notu)
        on2 = int(odev2_notu)
        fn = int(final_notu)
        ders_notu = v1y / 100 * v1n + v2y / 100 * v2n + o1y / 100 * on1 + o2y / 100 * on2 + final_yuzdesi / 100 * fn
        if (g >= 40):
            print("Geçme Notu 40, AA notu 85 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 40):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

        elif (g >= 50):

            print("Geçme Notu 50, AA notu 90 ve üzeri olarak ayarlanmıştır.")
            if (ders_notu >= 90):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: AA")

            elif (ders_notu >= 85):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BA")

            elif (ders_notu >= 80):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: BB")

            elif (ders_notu >= 75):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CB")

            elif (ders_notu >= 70):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: CC")


            elif (ders_notu >= 60):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DC")

            elif (ders_notu >= 50):
                print("Ders notunuz:", ders_notu, "\nHarf notunuz: DD", "\nŞartlı Geçtiniz.")
            else:
                print("Dersten kaldınız...")

bekle = input("")











