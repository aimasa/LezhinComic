import requests
import urllib.request as ulb
import random
import os
import json
import gzip
import zipfile
import glob
base_url = "https://cdn.lezhin.com/v2"

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
        'Referer': "https://www.lezhin.com/ko/comic/"+comic_name+"/"+series_id,
        'User-Agent': random.choice(my_headers)
    }

    for i in scrollsInfo:
        url = base_url + i['path']+"?access_token="+access_token+"&purchased=true&q=30&updated="+str(updatedAt);
        response = ulb.Request(url,headers=headers)
        print("第" +series_id + "话  " + "第" + str(index) + "张")
        file_name = base_dir + str(index) + ".jpg"
        data =ulb.urlopen(response, timeout=10).read()
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
               'referer':referer,
               'User-Agent': random.choice(my_headers),
               'cookie': lezhin_cookie}

    comic_info_request = ulb.Request(comic_info_entire_url, headers=headers)
    data = ulb.urlopen(comic_info_request,timeout=60).read()
    dic_data = json.loads(gzip.decompress(data).decode('utf-8'))
    return dic_data

def gain_group_comic_url_and_picture_number(dic_data):
    data = dic_data['data']
    extra = data['extra']
    episode = extra['episode']
    updatedAt = episode['updatedAt']
    scrollsInfo = episode['scrollsInfo']
    return updatedAt,scrollsInfo

def gain_comic_and_download(comic_chinese_name, comic_name,series_id, comic_id, lezhin_cookie, access_token, zip_type):
    comic_folder_name = "H:/"+ comic_chinese_name + series_id + "/"
    check_folder(comic_folder_name)
    dic_data = gain_comic_info_dic(comic_name, series_id, comic_id, lezhin_cookie)
    # 获取该漫画详细信息的json文件
    updatedAt, scrollsInfo = gain_group_comic_url_and_picture_number(dic_data)
    # 下载漫画当前话
    download(scrollsInfo, access_token, comic_folder_name, series_id, comic_name, updatedAt)
    # 压缩
    comic_zip_path = "H:/"+ comic_chinese_name
    check_folder(comic_zip_path)
    comic_zip_name = comic_chinese_name + series_id + "." + zip_type
    zip_path(comic_folder_name,comic_zip_path,comic_zip_name)

def zip_path(comic_folder_path, comic_zip_path,comic_zip_name):
    f = zipfile.ZipFile(comic_zip_path+'/'+comic_zip_name,'w',zipfile.ZIP_DEFLATED)
    files = glob.glob(comic_folder_path + '/*')
    for file in files:
        f.write(file)
    f.close()


if __name__ == "__main__":
    # -----------------------------------------------------
    # comic_chinese_name = "寻景镜头"
    # comic_name = "viewfinder"
    # series_id_first = 45
    # series_id_last = 46
    #------------------------------------------------------
    # comic_chinese_name = "我的哥哥我的老师"
    # comic_name = "mybromyssam"
    # series_id_first = 20
    # series_id_last = 20
    # ------------------------------------------------------
    comic_chinese_name = "小姐与王老五"
    comic_name = "snail"
    series_id_first = 103
    series_id_last = 110
    # ------------------------------------------------------
    zip_type = "zip"
    access_token = "7358890f-3291-404d-90e5-818c2eccf3c5"
    comic_id = "1567605913204"
    lezhin_cookie = "x-lz-locale=en_US; akaToken=ZXhwPTE1Njc2NDk1NTV+YWNsPSUyZnYyJTJmY29taWNzJTJmNTAzMDY1MDYyNDczNzI4MCUyZmVwaXNvZGVzJTJmNDkxMTI0Mzg2NDk2NTEyMCUyZmNvbnRlbnRzJTJmKnB1cmNoYXNlZCUzZGZhbHNlKn5obWFjPTRjZThlMjM1MTA4ZmM0NWZiNTQ3NTI0ZGM1ZGY4ZWI0MmEzOTJjOTFjNmQzODIwZWFmMDYzZjhmODBhMzYyN2Q=; AWSALB=kzZcbQG3UudIUeE8Zj+w3Xd4mEBiCUM8LGldz/P7h2LDix4A4xpcMoH990en+aWwZw2azRKrMOZ5RmCRooEiRZsSiQQTHG+Mloc353LHp2lzChDLBWRfizvgCxsl"
    for series_id in range(series_id_first,series_id_last + 1):
        gain_comic_and_download(comic_chinese_name, comic_name,str(series_id), comic_id, lezhin_cookie, access_token,zip_type)


