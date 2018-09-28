# resim url'si ile resim indiren kod
import urllib.request

url1="http://i.sozcu.com.tr/wp-content/uploads/2016/09/mustafa-kemal-ataturk.jpg"
url2="http://www.materyaller.com/img_up/Siyah-Beyaz-Ataturk-Fotograflari-22.jpg"
url3="https://postercim.net/image/cache/data/ATATURK_by_berk007-500x500.jpg"

urllist=[url1,url2,url3]
count=1

for url in urllist:
    urllib.request.urlretrieve(url,"Resim"+str(count)+".jpg")
    count+=1
print("indirmeler başarıyla gerçekleşti.")
