import random
import urllib.request as ulb
import check
import gzip
import json
import log
base_url = "https://cdn.lezhin.com/v2"
logging = log.lezhin_log(__name__).get_log()
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



def download(scrollsInfo, access_token, base_dir, series_id, comic_name, updatedAt):
    index = 1
    headers = {
        'Sec-Fetch-Mode': "no-cors",
        'Referer': "https://www.lezhin.com/ko/comic/" + comic_name + "/" + series_id,
        'User-Agent': random.choice(my_headers)
    }
    for i in scrollsInfo:
        url = base_url + i['path'] + "?access_token=" + access_token + "&purchased=true&q=30&updated=" + str(updatedAt);
        response = ulb.Request(url, headers=headers)
        print("第" + series_id + "话  " + "第" + str(index) + "张")
        file_name = base_dir + str(index) + ".jpg"
        data = ulb.urlopen(response, timeout=20).read()
        fp = open(file_name, "wb")
        fp.write(check.check_data(data,"lezhin的漫画文件"))
        fp.close()
        index = index + 1

def gain_comic_info(comic_name, series_id, comic_id, lezhin_cookie):
    comic_info_base_url = "https://www.lezhin.com/api/v2/inventory_groups/comic_viewer_a"
    referer = "https://www.lezhin.com/ko/comic/" + comic_name + "/" + series_id

    comic_info_entire_url = comic_info_base_url + "?platform=web&store=web&alias=" + comic_name + "&name=" + series_id + "&preload=true&type=comic_episode&_=" + comic_id
    headers = {'sec-fetch-mode': 'cors',
               'accept-encoding': 'gzip, deflate, br',
               'x-lz-locale': 'ko-KR',
               'accept-language': 'zh-CN,zh;q=0.9',
               'authorization': 'Bearer 7358890f-3291-404d-90e5-818c2eccf3c5',
               'x-lz-allowadult': 'true',
               'x-requested-with': 'XMLHttpRequest',
               'x-lz-adult': '1',
               'content-type': 'application/json',
               'accept': 'application/json, text/javascript, */*; q=0.01',
               'authority': 'www.lezhin.com',
               'x-lz-country': 'jp',
               'sec-fetch-site': 'same-origin',
               'referer': referer,
               'User-Agent': random.choice(my_headers),
               'cookie': lezhin_cookie}

    comic_info_request = ulb.Request(comic_info_entire_url, headers=headers)
    data = ulb.urlopen(comic_info_request, timeout=60).read()
    check.check_data(data,"lezhin响应漫画信息的json文件")
    dic_data = json.loads(gzip.decompress(data).decode('utf-8'))
    return dic_data