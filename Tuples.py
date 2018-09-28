# Tuples #

TupleFener = ("Harun","Skirtel","Reyes","Şener","Hasan Ali","Ayew","Eljif","Jailson","Barış Alıcı","Benzia","Slimani")
print(type(TupleFener))
print(TupleFener)
print(len(TupleFener))

# tek elemanlı tuple tanımlaması #
print("\nTek Elemanlı Tuple Tanımlamak:","TekElemanli = ('İlk Eleman',)")
TekElemanli = ("İlk Eleman",)
print(type(TekElemanli))
print(TekElemanli)
# tek elemanlı tuple tanımlaması #

# Tupleslerde atama işlemi #
print("\nTupleFenerin elemanları kaleci stoper vs.. tutucularına atılıyor..")
kaleci,stoper1,stoper2,sagbek,solbek,sagacik,ortasaha1,ortasaha2,solacik,forvetarkasi,forvet=TupleFener
print(kaleci)
print(stoper1)
# Tupleslerde atama işlemi #

#Listelerde de aynı işlem yapılabiliyor #
print("\nListelerde tuples gibi atama yapılabiliyor: List1=[1,2,3] sayi1,sayi2sayi3=List1")
List1=[1,2,3]
sayi1,sayi2,sayi3=List1
print("sayi1:",sayi1)
#Listelerde de aynı işlem yapılabiliyor #

# boş tuple #
print("\nBOŞ tuple tanımı: Demet=()")
Demet = ()
print(type(Demet))
# boş tuple #
