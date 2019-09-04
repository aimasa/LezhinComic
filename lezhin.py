import requests
import urllib.request as ulb
import random
from selenium import webdriver
base_url = "https://cdn.lezhin.com/v2/comics/6027140077846528/episodes/6539198023467008/contents/scrolls/"

base_dir = "H:/寻景镜头/32"
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


def download(picture_number):
    for i in range(1, picture_number + 1):
        opener = ulb.build_opener()
        url = base_url + str(i);
        response = ulb.Request(url)
        response.add_header('User-Agent', random.choice(my_headers))
        response.add_header('cookie',
                            "_ga=GA1.2.185010817.1567496059; _gid=GA1.2.992340615.1567496059; cto_lwid=60ea1905-a9df-47c0-86da-19cda1118d1a; x-lz-locale=ko_KR; _gcl_au=1.1.1263518645.1567496352; _BS_GUUID=ilxAIykH5ElUwlzyBsHYnD9uYTzN5mjnIQYqoj8t; _fbp=fb.1.1567496355651.1709111557; _dg_t1_ses.99fc=*; _TRK_AUIDA_14106=215877072b25271ab0449b207e5f6b93:3; _TRK_ASID_14106=f3de9d11bb00b8c09202c4b972e09aab; cc=mP-3DGkriVbLlhkRTGi9RreJuyUWVU1rlekm8gMjJOM2mHyXC7JGtDzRiwvptZUUwGS8GlLwmdvGgMh_JlkR4W3Qb4Nel9K8ulwtSJ-pIso9SAKIJ7yV7Sx2f47Kl_MrnqPzxAYda-eUHnHZoOiXkbwej5HPDUTzu7LqFTRWKpU; AWSALB=fObHcHLVSPXBCRul5/rg8GPI+ukF/QaIBMfEVHLi3yPTD8UXnmngQTguzcTlAhvtjgpG1zZa0TyhK54AwyG7qfJCNDezjeLDHOoJzCDt4kKlatBB4cFmjkeA6xnH; akaToken=ZXhwPTE1Njc1MTY0MDl+YWNsPSUyZnYyJTJmY29taWNzJTJmNTc5MDcxMTUwMTQyMjU5MiUyZmVwaXNvZGVzJTJmNjIwNzY0MjkwMTU0NDk2MCUyZmNvbnRlbnRzJTJmKnB1cmNoYXNlZCUzZCp+aG1hYz00ZTdlMDZjYzE4NWZlMWE3NThlY2EzMjQxNDg4ZTI0Zjk0ZmZhMDQ3YmFlMThhOWFmYjdiMDJiZjRmMjBlMGQ4; _dg_t1_id.99fc=791317f3-ab96-411f-86e9-b37508acfd20.1567496240.3.1567516138.1567510972.c4f8805f-f595-4d05-97e3-d34f069d43af")
        print("第" + str(i) + "话")
        file_name =base_dir + str(i) + ".jpg"
        data = ulb.urlopen(response).read()
        fp = open(file_name,"wb")
        fp.write(data)
        fp.close()



if __name__ == "__main__":
    download(15)

