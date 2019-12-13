from bs4 import BeautifulSoup

import webbrowser
import urllib.request # python3x request kütüphanesi
#url belirtelim.
url = "https://www.selcuk.edu.tr/saglik_kultur/birim/web/sayfa/ayrinti/1473/tr"
#url'i okuyalum.
url_oku = urllib.request.urlopen(url)
#BeautifulSoup yollyalım.
soup = BeautifulSoup(url_oku, 'html.parser')
# tüm html dökümanı ekrana basalım
	
ana = soup.find('span',attrs={"id": "ContentPlaceHolder1_lblIcerik"})

resim=ana.find('img')
resimac=resim['src']


webbrowser.open_new(resimac)
