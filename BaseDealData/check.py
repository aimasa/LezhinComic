from RunInfo import log
from RunInfo.error import UseError
import os
logging = log.lezhin_log(__name__).get_log()

def check_data(data, data_name):

    if isinstance(data, str):
        if data.strip():
            logging.debug("%s : %s 数据已传入", data_name, data)
            return data
        else:
            logging.error("%s 数据缺失", data_name)
            raise UseError("数据缺失，详情见log日志")
            pass

    elif isinstance(data, list):
        if data:
            logging.debug("%s : %s 数据已传入", data_name, data)
            return data
        else:
            logging.error("%s 数据缺失", data_name)
            raise UseError("数据缺失，详情见log日志")
    elif isinstance(data, dict):
        if data:
            logging.debug("%s : %s 数据已传入", data_name, data)
            return data
        else:
            logging.error("%s 数据缺失", data_name)
            raise UseError("数据缺失，详情见log日志")
            pass
    elif isinstance(data,int):
        if data:
            if data >= 0:
                logging.debug("%s : %s 数据已传入", data_name, data)
                return data
            else:
                logging.debug("%s : %s 数据传入不规范", data_name, data)
                raise UseError("输入数据过小，详情请见log日志")
        else:
            logging.error("%s 数据缺失", data_name)
            raise UseError("数据缺失，详情见log日志")
            pass
    return data

def check_series_id(series_id_first,series_id_last):

    if series_id_last < series_id_first:
        logging.error("需要下载的第一章id %s 大于需要下载的最后一章id %s，需要对想要下载的章节id重新设置",series_id_first,series_id_last)
        raise UseError("章节设置错误，详情见log日志")
    else:
        pass

def check_folder(comic_folder_name):
    if os.path.exists(comic_folder_name):
        pass
    else:
        os.makedirs(comic_folder_name)