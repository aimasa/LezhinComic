# import requests
#
# url = "https://cdn.lezhin.com/v2/comics/6027140077846528/episodes/5880423793688576/contents/scrolls/2"
#
# querystring = {"access_token":"7358890f-3291-404d-90e5-818c2eccf3c5","purchased":"true","q":"30","updated":"1553482801895"}
#
# headers = {
#     'Sec-Fetch-Mode': "no-cors",
#     'Referer': "https://www.lezhin.com/ko/comic/viewfinder/2",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# fp = open("./test2.jpeg", "wb")
# fp.write(response.content)
# fp.close()
# 压缩文件脚本
import zipfile
import glob
def zip_path(comic_folder_path, comic_zip_path,comic_zip_name):
    f = zipfile.ZipFile(comic_zip_path+'/'+comic_zip_name,'w',zipfile.ZIP_DEFLATED)
    files = glob.glob(comic_folder_path + '/*')
    for file in files:
        f.write(file)
    f.close()
'''
'''
if __name__ == "__main__":
    for i in range(18,21):
        comic_folder_path = "H:/我的哥哥我的老师"+str(i)
        comic_zip_path = "H:/我的哥哥我的老师"
        comic_zip_name = "我的哥哥我的老师"+str(i)+".zip"
        zip_path(comic_folder_path, comic_zip_path,comic_zip_name)