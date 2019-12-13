from bs4 import BeautifulSoup
import webbrowser
import urllib.request 

url = "https://www.selcuk.edu.tr/saglik_kultur/birim/web/sayfa/ayrinti/1473/tr"
url_oku = urllib.request.urlopen(url)

soup = BeautifulSoup(url_oku, 'html.parser')

ana = soup.find('span',attrs={"id": "ContentPlaceHolder1_lblIcerik"}) #span etiketinde aradağımız id değerini bulalım
resim=ana.find('img') # resimleri bulalım
resimac=resim['src'] 


webbrowser.open_new(resimac)
