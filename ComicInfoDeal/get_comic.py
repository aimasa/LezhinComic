from BaseDealData import check, deal_data
from RunInfo import log
from ComicInfoDeal import mock_request

logging = log.lezhin_log(__name__).get_log()
def gain_comic_to_download_and_zipfile(comic_chinese_name, comic_name, series_id, comic_id, lezhin_cookie, access_token, zip_type,
                            folder_name_header):
    comic_folder_name = folder_name_header + comic_chinese_name + "/" + comic_chinese_name + series_id + "/"
    try:
        check.check_folder(comic_folder_name)
    except Exception as e:
        logging.error("创建存储漫画文件夹失败,原因：%s",e)
    dic_data = mock_request.gain_comic_info(comic_name, series_id, comic_id, lezhin_cookie)
    # 获取该漫画详细信息的json文件
    updatedAt, scrollsInfo = deal_data.gain_info_from_dic(dic_data)
    # 下载漫画当前话
    mock_request.download(scrollsInfo, access_token, comic_folder_name, series_id, comic_name, updatedAt)
    # 压缩
    comic_zip_path = folder_name_header + comic_chinese_name
    check.check_folder(comic_zip_path)
    comic_zip_name = comic_chinese_name + series_id + "." + zip_type
    deal_data.zip_to_folder(comic_folder_name, comic_zip_path, comic_zip_name)

