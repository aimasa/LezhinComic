import requests
import urllib.request as ulb
import random
import os
import json
import gzip

base_url = "https://cdn.lezhin.com/v2"

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


def download(scrollsInfo, lezhin_cookie, base_dir, series_id):
    index = 1
    for i in scrollsInfo:
        url = base_url + i['path'] + "?access_token=7358890f-3291-404d-90e5-818c2eccf3c5&purchased=true&q=30&updated=1553482801895";
        response = ulb.Request(url)
        response.add_header('User-Agent', random.choice(my_headers))
        response.add_header('cookie', lezhin_cookie)
        print("第" +series_id + "话  " + "第" + str(index) + "张")
        file_name = base_dir + str(index) + ".jpg"
        data = ulb.urlopen(response).read()
        fp = open(file_name, "wb")
        fp.write(data)
        fp.close()
        index = index + 1


def check_folder(comic_folder_name):
    if os.path.exists(comic_folder_name):
        pass
    else:
        os.makedirs(comic_folder_name)


def gain_comic_info_dic(comic_name, series_id, comic_id, lezhin_cookie):
    comic_info_base_url = "https://www.lezhin.com/api/v2/inventory_groups/comic_viewer_a"

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
               'sec-fetch-site': 'same-origin'}
    referer = "https://www.lezhin.com/ko/comic/" + comic_name + "/" + series_id
    comic_info_request = ulb.Request(comic_info_entire_url, headers=headers)
    comic_info_request.add_header('referer', referer)
    comic_info_request.add_header('User-Agent', random.choice(my_headers))
    comic_info_request.add_header('cookie', lezhin_cookie)
    data = ulb.urlopen(comic_info_request,timeout=30).read()

    dic_data = json.loads(gzip.decompress(data).decode('utf-8'))
    return dic_data

def gain_group_comic_url_and_picture_number(dic_data):
    data = dic_data['data']
    extra = data['extra']
    episode = extra['episode']
    scroll = episode['scroll']
    scrollsInfo = episode['scrollsInfo']
    return scroll,scrollsInfo

def gain_comic_and_download(comic_chinese_name, comic_name,series_id, comic_id, lezhin_cookie):
    comic_folder_name = "H:/"+ comic_chinese_name + series_id + "/"
    check_folder(comic_folder_name)
    dic_data = gain_comic_info_dic(comic_name, series_id, comic_id, lezhin_cookie)
    scroll, scrollsInfo = gain_group_comic_url_and_picture_number(dic_data)
    download(scrollsInfo, lezhin_cookie, comic_folder_name, series_id)


if __name__ == "__main__":
    # -----------------------------------------------------
    # comic_chinese_name = "寻景镜头"
    # comic_name = "viewfinder"
    # series_id_first = 45
    # series_id_last = 46
    #------------------------------------------------------
    # comic_chinese_name = "我的哥哥我的老师"
    # comic_name = "mybromyssam"
    # series_id_first = 17
    # series_id_last = 19
    # ------------------------------------------------------
    comic_chinese_name = "小姐与王老五"
    comic_name = "snail"
    series_id_first = 103
    series_id_last = 110
    # ------------------------------------------------------

    comic_id = "1567605913204"
    lezhin_cookie = "x-lz-locale=ko_KR; _ga=GA1.2.394601603.1567604555; _gid=GA1.2.1191437402.1567604555; cto_lwid=4ba946fd-332a-4bce-9dbf-581af43fcda0; _dg_t1_ses.99fc=*; _gcl_au=1.1.1760066550.1567604555; _fbp=fb.1.1567604555487.1110827021; JSESSIONID=4yr6QqKY36ojsiwKyNwhaQ; _BS_GUUID=ilxAIykH5ElUwlzyBsHYnD9uYTzN5mjnIQYqoj8t; _TRK_AUIDA_14106=0c24fc95a33400c7d0d55ea4d57c2080:1; _TRK_ASID_14106=1a02158c6bf8fcd151eaa31fef08c74a; REMEMBER=c2lqaW5yZW5jYW9AZ21haWwuY29tOjE1NzAxOTc3MjA0Mzk6MThjY2U1ZmJiYTgwYjc4N2I1M2U4ZTg2YmJkMDU1MWM; akaToken=ZXhwPTE1Njc2MDYxOTl+YWNsPSUyZnYyJTJmY29taWNzJTJmNjAyNzE0MDA3Nzg0NjUyOCUyZmVwaXNvZGVzJTJmNTg4MDQyMzc5MzY4ODU3NiUyZmNvbnRlbnRzJTJmKnB1cmNoYXNlZCUzZHRydWUqfmhtYWM9NGVjNjRiMGE3ZmRkODk1YTU3OGJmNmQyN2RhM2U0ZTNmNTM4MjYyZjFhYTAyYjUyZWZiNThiOTJiOTViZWRmOQ==; _dg_t1_id.99fc=67df5914-2c41-4ae7-803c-50b3beaa627d.1567604555.1.1567605899.1567604555.da526573-2c0a-48ae-9281-13740ba3885e; _gali=btn-yes; cc=mP-3DGkriVbLlhkRTGi9RkchsGJ1p_VUUetQL--YL70Xnu35MmOCR1tXkBo1VlmlQ0UPmttMujZRu46R-xTRROpyTu_06maQUUxvgE1h3SZDNsdYQUUi4HCbEeugW0xMY7z6KAGJryoehv8abmwiZe2QhFKOE2bVNtIBSrDenT3IocNwrNnQ7AWV6Ns4B7Pw; AWSALB=zdpL3E7hwRSkvXeqjF2EJq45+OOwZUljofB7tL4MGcnFGI9y3FmX5+klDZQQWs7hklmKmXhZGMWjb1Y9G6rI/jsN+fNu1DpwEI2I+yrdXpYvqJFSF08pOkZAS99G0PdTJZNHevZxhljkugBJmZFxjTv+fEVputZ2y2aYR+uf1Y1qKxKGslng/2+HPyxXLA==; RSESSION=L25vRklPWWJVdjdEOWVFMnQzZFNUQVh5aVRWb3ZFbVhiN3o3bUg2dWFYRllnWEd4cEFsOXNHSHhvZHBGSXo2M2x4WFJWZmoxV1kvSDZkZWFGQTFrUUNZVmpoWk16cG1GOXh2cUN4VUVFNTVIeGl2dGVERFk2NnI2OVFodVZxMVh3a1c1MkJrQkFNbkYwZFhGTkxYWmdUN0xPc1pJWm9PTUV0TkNOV0NvRm5xeWJMZ1FIb1FTNjd6YW9CSTI4R0hwS2VmZVBZOW1NeHRnOC8wOVBSd0dBdXl3OGNncXVEKzVkTVNOcjhuSHE5Vm1jWEdIcmpoRlJOcDA2N1F0OXp0MCtJOE51ZmtsVU54SWVwdXM0anNhK0s5cG9PUk41OFhUL1k5dkJPNGQvN2xCdXNqOWd4d2F0ZGtVZk44QlNWWTBVS0w5cVB1cmJuWDFkNGVVY3pDbXkvMDk5QjI0ZkVXSVUzYVBwTnZSbGU5M3puRUJpeC8ybm1USGZkV0E5cTA4LS0wSm5XUVlKMnVRb3pnYTNyVHpZa3lRPT0^%^3D--e1d3a8a7a01e8fe7c6b4ab4de23567a9bb3b4cc7"
    for series_id in range(series_id_first,series_id_last + 1):
        gain_comic_and_download(comic_chinese_name, comic_name, str(series_id), comic_id, lezhin_cookie)
