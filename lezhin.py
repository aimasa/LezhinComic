import time
import deal_data
import check
import log
import get_comic
logging = log.lezhin_log(__name__).get_log()
def run(config_url):
    config = deal_data.read_config(config_url)
    comic_chinese_name = check.check_data(config['comic_info']['comic_chinese_name'].strip(),"comic_chinese_name")
    comic_name = check.check_data(config['comic_info']['comic_name'].strip(),"comic_name")
    series_id_first = check.check_data(config['comic_info']['series_id_first'].strip(),"series_id_first")
    series_id_last = check.check_data(config['comic_info']['series_id_last'].strip(),"series_id_last")
    comic_id = check.check_data(config['comic_request_info']['comic_id'].strip(),"comic_id")
    lezhin_cookie = check.check_data(config['comic_request_info']['lezhin_cookie'].strip(),"lezhin_cookie")
    access_token = check.check_data(config['comic_request_info']['access_token'].strip(),"access_token")
    zip_type = check.check_data(config['folder_info']['zip_type'].strip(),"zip_type")
    folder_name_header = check.check_data(config['folder_info']['folder_name_header'].strip(),"folder_name_header")
    check.check_series_id(series_id_first,series_id_last)
    for series_id in range(int(series_id_first), int(series_id_last) + 1):
        get_comic.gain_comic_to_download_and_zipfile(comic_chinese_name, comic_name, str(series_id), comic_id, lezhin_cookie, access_token,
                                zip_type, folder_name_header)
        if str(series_id) == series_id_last:
            logging.debug("下载完第%s章，休息20s",str(series_id))
            time.sleep(20)

if __name__ == "__main__":
    run("H:\comic_info.ini")


