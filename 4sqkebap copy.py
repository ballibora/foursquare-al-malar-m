import requests
import json

url = 'https://api.foursquare.com/v2/venues/search'
# konu=input("konu girin:")
# sehir=input("şehir girin:")
konu = "tantuni"
sehir= "mersin"
params = dict(
   client_id='', #client id buraya girilecek
   client_secret='',#client secret buraya girilecek
   v='20191214',
   near = sehir,
   query = konu,

   limit = 20
)

response = requests.get(url = url, params = params)

data = json.loads(response.text)

if data["meta"]["code"] == 200 :
    print("veri alınıyor.\n")
else :
    print("Hata.\n")

sira = 1
mekanlar = []
for i in data["response"]["venues"]:

    mekan = i["name"]
    print(f"{sira} - {mekan}")
    mekanlar.append(i["id"])

    sira = sira +1

secim = int(input("hangi mekanın detaylarını görmek istersiniz: "))
    
id = mekanlar[secim-1]


detail_url = "https://api.foursquare.com/v2/venues/"+id
params = dict(
   client_id='FDVNH2D1ITQ5VPFHAWMGNRNELZZFV123I5YYGYQW4P1G3GIG', 
   client_secret='4SGIODLEEEFQXJY4TVSYGIVSH5B4TOC4531A215THD5B4PN3',
   v='20191214'
)

detail_response = requests.get(url = detail_url, params = params)

detail_data = json.loads(detail_response.text)


print(detail_data['response']['venue']['contact']['formattedPhone'])
print(detail_data['response']['venue']['location']['formattedAddress'])

if "twitter" in detail_data['response']['venue']['contact']:
    print(detail_data['response']['venue']['contact']['twitter'])
if "facebook" in detail_data['response']['venue']['contact']:
    print(detail_data['response']['venue']['contact']['facebook'])
