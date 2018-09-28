##################################### List's ###################################
List1= [1,"Göktürk",2,"Saltuk Buğra",3,"Mustafa Kemal",4,"Timur"]
List2= [1,"Türkiye Cumhuriyeti",2,"Osmanlı İmp.",3,"Selçuklu Devleti",4,"Göktürkler"]

print("Listelerin indislenmesi de aynı stringlerin indislenmesi gibidir.")
print("Liste1[1]:Göktürk basmasını bekleriz:",List1[1])
print("Liste[1:] 1. indisten sona kadar basmasını bekleriz:",List1[1:])
print("Liste2[::-1] tersten sona doğru basmasını bekleriz:",List2[::-1])
print("Liste2[1:5] 1.indisten 5. indis'e kadar basmasını bekleriz 5. indis dahil değil:",List2[1:5])
##################################### List's ###################################

# # List's Fonk.ları 
# index() fonk 
print("\n\n\nindex() fonk kullanımı:","List2.index('Osmanlı İmp.'):",List2.index("Osmanlı İmp."))
# index() fonk #

# append() fonk #
print("\nappend uygulanmadan önce List1:",List1)
List1.append(5)
print("\n\n\nListelerde append() fonk kullanımı:","List1.append(5):",List1)
# append() fonk #

# extend() fonk #
List1.extend(["Ataman",6,"Ertuğrul",7,"Gökbörü"])
print("\nListelerde extend() fonk kullanımı:","List1.extend(['Ataman',6,'Ertuğrul',7,'Gökbörü']):",List1)
print("\n\nremove uygulanmadan önce List2:",List2)
# extend() fonk #

# remove() fonk #
List2.remove("Osmanlı İmp.")
print("\nListelerde remove() fonk. kullanımı:","List2.remove('Osmanlı İmp.'):",List2)
# remove() fonk #

# insert() fonk #
print("\ninsert() fonk uygulanmadan önce List2:",List2)
List2.insert(3,"Osmanlı İmp.")
print("insert işlemi sonrasında List2:",List2)
# insert() fonk #

# pop() fonk #
print("\npop() uygulanmadan önce List1:",List1)
print(List1.pop())
print("pop fonk kullanımı:","List1.pop():",List1)
print("eğer pop() içine parametre atanmazsa son elemanı diziden çıkarır ve o elemanı döndürür.")
print("paramtre atanırsa o parametrenin indexindeki elemanı çıkarır ve döndürür:","List1.pop(0):",List1.pop(0))
print(List1)
# pop() fonk #

# sort() fonk #

Harfler = ['t','ü','r','k']
print("\n sort() fonk kullanımından önce Harfler:",Harfler)
Harfler.sort()
print("sort fonk kullanıldıktan sonra:",Harfler)
# sort() fonk #

# reverse() fonk #

print("\nReverse Fonk kullanılmadan önce harfler:",Harfler)
Harfler.reverse()
print("reverse fonk kullanıldıktan sonra:",Harfler)
# reverse() fonk #

# 'in' ve 'not in' kullanımı #

print("\n'in' sorgusunda yapılan öge listede varsa true yoksa false döner.\n 'not in' sorgusu yapılan öge listede yoksa true varsa false döner")
Turkiye=["yolsuzluk","terör","işsizlik","kriz","adam kayırma","rüşvet","mülteci"]
print(Turkiye)
print("\n Türkiye'de yolsuzluk var mıdır sorgusu şöyle yapılır:","'yolsuzluk' in Turkiye:")
var_mıdır="yolsuzluk" in Turkiye
print(var_mıdır)
print("Turkiye'de adalet var mıdır:","'adalet' in Turkiye:",'adalet' in Turkiye)
Teror = ["pkk","işid","fetö","bokoharam","elkaide","abd","israil","çin","rusya"]
print("\nListe toplamadan önce terör:",Teror)

# 'in' ve 'not in' kullanımı #

# split() fonk #

Atis_Yapilacak_Silahlar ="g3,mp5,sarsılmaz,ak47,m4,m16,rpg7,seasparrow"
Silahlar = Atis_Yapilacak_Silahlar.split(',')
print("\n\nString ifadeyi split(',') fonk ile virgüle göre ayırarak diziye atıyoruz.")
print("dizi:",Atis_Yapilacak_Silahlar,"\n","Liste:",Silahlar)
# split() fonk #

# del işlemi #

a_tarihi = ["f","şantaj","tehdit","kumpas","asker düşmanlığı","terör seviciliği",17,25]
print("\nnormalde a_tarihi:",a_tarihi)
del a_tarihi[0]
print(" a_tarihi'nden fyü silme çabası: del a_tarihi[0]:",a_tarihi)
# del işlemi #

# Listelerde eşitlik #

fe =["kumpas","şantaj","gericilik"]
a=fe
print("\na ve fe esitledik")
print("\nFe:",fe,"\na:",a)
fe.append("din tüccarlığı")
print("feye din tüccarlıgı append ettik bakalım aye de etki etmiş mi?\nFe:",fe,"\nA:",a)
fe=["teror orgutu"]
print("\nFe yeniden tanımlanınca:",fe,"\nA:",a)
# Listelerde eşitlik #

