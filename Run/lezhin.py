import time
from BaseDealData import check, deal_data
from RunInfo import log
from ComicInfoDeal import get_comic

logging = log.lezhin_log(__name__).get_log()
def run(config_url):
    config = deal_data.read_config(config_url)
    comic_chinese_name = check.check_data(config['comic_info']['comic_chinese_name'].strip(), "comic_chinese_name")
    comic_name = check.check_data(config['comic_info']['comic_name'].strip(), "comic_name")
    series_id_first = check.check_data(config['comic_info']['series_id_first'].strip(), "series_id_first")
    series_id_last = check.check_data(config['comic_info']['series_id_last'].strip(), "series_id_last")
    comic_id = check.check_data(config['comic_request_info']['comic_id'].strip(), "comic_id")
    lezhin_cookie = check.check_data(config['comic_request_info']['lezhin_cookie'].strip(), "lezhin_cookie")
    access_token = check.check_data(config['comic_request_info']['access_token'].strip(), "access_token")
    zip_type = check.check_data(config['folder_info']['zip_type'].strip(), "zip_type")
    folder_name_header = check.check_data(config['folder_info']['folder_name_header'].strip(), "folder_name_header")
    spare_time = check.check_data(config['spare_time']['spare_time'].strip(),"spare_time")
    check.check_series_id(series_id_first, series_id_last)
    for series_id in range(int(series_id_first), int(series_id_last) + 1):
        logging.debug("下载第 %d 话",series_id)
        get_comic.gain_comic_to_download_and_zipfile(comic_chinese_name, comic_name, str(series_id), comic_id, lezhin_cookie, access_token,
                                                     zip_type, folder_name_header)
        if str(series_id) == series_id_last:
            logging.debug("下载完第%s章，休息 %s s",str(series_id),spare_time)
            time.sleep(int(spare_time))

if __name__ == "__main__":
    run("H:\comic_info.ini")


