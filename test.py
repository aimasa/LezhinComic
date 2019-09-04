import requests

url = "https://cdn.lezhin.com/v2/comics/6027140077846528/episodes/5880423793688576/contents/scrolls/1"

querystring = {"access_token":"7358890f-3291-404d-90e5-818c2eccf3c5","purchased":"true","q":"30","updated":"1553482801895"}

headers = {
    'Sec-Fetch-Mode': "no-cors",
    'Referer': "https://www.lezhin.com/ko/comic/viewfinder/2",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
}

response = requests.request("GET", url, headers=headers, params=querystring)
fp = open("./test.jpeg", "wb")
fp.write(response.content)
fp.close()