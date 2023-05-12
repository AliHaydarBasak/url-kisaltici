import pyshorteners

# url = input("Bir URL girin: ")

# if "https" and "https" not in url:
#     url = "https://"+url

# key = 'accsess_key'

# metot = pyshorteners.Shortener(api_key= key)

# kisaltilmis_url = metot.bitly.short(url)

# print(f"kısaltılmış URL: {kisaltilmis_url}")


url = input("Bir URL girin: ")
#url='https://www.youtube.com/watch?v=SZS7Y9GXl3c'

if "https" and "https" not in url:
     url = "https://"+url

kisa = pyshorteners.Shortener()
kisa_url = kisa.tinyurl.short(url)
print('kısaltılmış URL: ', kisa_url )