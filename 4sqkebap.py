import requests
import json

url = 'https://api.foursquare.com/v2/venues/search'
konu=input("konu girin:")
sehir=input("şehir girin:")

params = dict(
   client_id='', #client id buraya gelecek 
   client_secret='', #client secret buraya gelecek
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
   client_id='', #client id buraya gelecek 
   client_secret='', #client secret buraya gelecek
   v='20191214'
)

detail_response = requests.get(url = detail_url, params = params)

detail_data = json.loads(detail_response.text)

adres = ""

for i in detail_data["response"]["venue"]["location"]["formattedAddress"]:

    adres = adres+" "+i
    

isim = detail_data["response"]["venue"]["name"]
kategori = detail_data["response"]["venue"]["categories"][0]["name"]
fiyat = detail_data["response"]["venue"]["price"]["message"]
rating = detail_data["response"]["venue"]["rating"]
yorum =[]
günler = []
saatler = []

for i in detail_data["response"]["venue"]["tips"]["groups"][0]["items"]:
    yorum.append(i["text"])

for i in detail_data["response"]["venue"]["popular"]["timeframes"]:

    günler.append(i["days"])
    saatler.append(i["open"][0]["renderedTime"])

# for i in detail_data["response"]["venue"]["attributes"]["groups"]:
#     if "payments" in i["type"].values() :
#         kart = i["items"][0]["displayValue"]

#     elif "wifi" in i["type"].values():
#         wifi = i["items"][0]["displayValue"]

print(f"isim: {isim}\nkategori: {kategori}\nfiyat: {fiyat}\nrating: {rating}")
print("yorumlar:")
for i in yorum:
    print(i)
print("açık olduğu günler:")

döngü=0
for i in günler:
    a= i +": "+saatler[döngü]
    print(a)
    döngü = döngü+1
